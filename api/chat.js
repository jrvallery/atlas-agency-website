// Vercel Edge Function — proxies chat to local OpenClaw gateway via Cloudflare tunnel.
// Handles CORS, rate limiting, and keeps the auth token server-side.

export const config = { runtime: 'edge' };

const GATEWAY = process.env.GATEWAY_URL || 'https://haven-weights-definition-types.trycloudflare.com';
const TOKEN   = process.env.GATEWAY_TOKEN || '16cf6ab57c4ed94f2f0b114a84e1fb31a8752765c49bb350';
const AGENT   = 'atlas-demo';

// Rate limit: 15 requests per IP per 5 minutes (best-effort, in-memory per edge node)
const RATE_LIMIT    = 15;
const WINDOW_MS     = 5 * 60 * 1000;
const MAX_MSG_LEN   = 500;
const MAX_HISTORY   = 12;

const ipMap = new Map();

function isRateLimited(ip) {
  const now  = Date.now();
  const entry = ipMap.get(ip) || { count: 0, reset: now + WINDOW_MS };
  if (now > entry.reset) { entry.count = 0; entry.reset = now + WINDOW_MS; }
  entry.count++;
  ipMap.set(ip, entry);
  return entry.count > RATE_LIMIT;
}

export default async function handler(req) {
  if (req.method === 'OPTIONS') return new Response(null, { status: 204, headers: cors() });
  if (req.method !== 'POST') return new Response('Method not allowed', { status: 405 });

  // Rate limiting
  const ip = req.headers.get('x-forwarded-for')?.split(',')[0].trim() || 'unknown';
  if (isRateLimited(ip)) {
    return new Response(JSON.stringify({ error: 'Too many requests. Please slow down!' }), {
      status: 429, headers: { 'Content-Type': 'application/json', 'Retry-After': '60', ...cors() }
    });
  }

  let body;
  try { body = await req.json(); } catch {
    return new Response(JSON.stringify({ error: 'Invalid request' }), { status: 400, headers: cors() });
  }

  // Sanitize: cap history length and message size
  let messages = (body.messages || []).slice(-MAX_HISTORY);
  messages = messages.map(m => ({
    role: m.role,
    content: typeof m.content === 'string' ? m.content.slice(0, MAX_MSG_LEN) : ''
  }));

  try {
    const upstream = await fetch(`${GATEWAY}/v1/chat/completions`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${TOKEN}`,
        'x-openclaw-agent-id': AGENT,
      },
      body: JSON.stringify({ model: 'openclaw', stream: true, messages }),
    });

    return new Response(upstream.body, {
      status: upstream.status,
      headers: { 'Content-Type': 'text/event-stream', 'Cache-Control': 'no-cache', ...cors() },
    });
  } catch {
    return new Response(JSON.stringify({ error: 'Gateway unreachable' }), {
      status: 502, headers: { 'Content-Type': 'application/json', ...cors() }
    });
  }
}

function cors() {
  return {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
  };
}
