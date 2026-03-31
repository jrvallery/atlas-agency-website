// Vercel Edge Function — proxies chat requests to the local OpenClaw gateway
// via Cloudflare tunnel. Keeps the auth token server-side and solves CORS.

export const config = { runtime: 'edge' };

const GATEWAY = process.env.GATEWAY_URL || 'https://haven-weights-definition-types.trycloudflare.com';
const TOKEN   = process.env.GATEWAY_TOKEN || '16cf6ab57c4ed94f2f0b114a84e1fb31a8752765c49bb350';
const AGENT   = 'atlas-demo';

export default async function handler(req) {
  if (req.method === 'OPTIONS') {
    return new Response(null, { status: 204, headers: cors() });
  }
  if (req.method !== 'POST') {
    return new Response('Method not allowed', { status: 405 });
  }

  try {
    const body = await req.json();
    const upstream = await fetch(`${GATEWAY}/v1/chat/completions`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${TOKEN}`,
        'x-openclaw-agent-id': AGENT,
      },
      body: JSON.stringify({ ...body, stream: true }),
    });

    return new Response(upstream.body, {
      status: upstream.status,
      headers: {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache',
        ...cors(),
      },
    });
  } catch (err) {
    return new Response(JSON.stringify({ error: 'Gateway unreachable' }), {
      status: 502,
      headers: { 'Content-Type': 'application/json', ...cors() },
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
