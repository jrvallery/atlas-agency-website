import re

with open('/home/james/atlas/website/index.html', 'r') as f:
    content = f.read()

old_section = """<section class="py-20 px-4">
        <div class="max-w-3xl mx-auto text-center">
            <h2 class="text-3xl font-extrabold mb-4">See It In Action: Meet "Mario"</h2>
            <p class="text-gray-400 mb-10">Chat with our live demo OpenClaw agent. Mario is configured to act as an automated dispatcher for a plumbing business. Try asking him to book a pipe repair or about his services!</p>
            <div id="chat-widget" class="bg-slate border-2 border-dashed border-electric/40 rounded-2xl min-h-[420px] flex flex-col items-center justify-center text-gray-500 relative overflow-hidden">
                <!-- Animated bg effect -->
                <div class="absolute inset-0 bg-gradient-to-br from-electric/5 to-transparent pointer-events-none"></div>
                <div class="relative z-10 flex flex-col items-center gap-4 p-8">
                    <div class="w-16 h-16 bg-red-500/10 border border-red-500/30 rounded-2xl flex items-center justify-center text-3xl">
                        🍄
                    </div>
                    <p class="text-lg font-semibold text-gray-300">Mario Demo Widget</p>
                    <p class="text-sm text-gray-500 max-w-xs text-center">This area will load the live Mario OpenClaw agent once the connection to your demo VM is configured.</p>
                    <a href="contact.html" class="mt-2 bg-electric/20 hover:bg-electric/30 border border-electric/40 text-accent font-medium px-5 py-2.5 rounded-lg text-sm transition-colors">Talk to a human instead →</a>
                </div>
            </div>
        </div>
    </section>"""

new_section = """<section class="py-20 px-4">
        <div class="max-w-3xl mx-auto text-center">
            <h2 class="text-3xl font-extrabold mb-4">Chat with the Atlas Co-pilot</h2>
            <p class="text-gray-400 mb-10">This agent is built on the exact same technology we deploy for our clients. Ask it about our pricing, services, or how managed AI hosting works!</p>
            
            <!-- OpenClaw Webchat Container -->
            <div id="openclaw-webchat-container" class="bg-slate border border-electric/40 rounded-2xl h-[500px] flex flex-col overflow-hidden shadow-2xl shadow-blue-900/20 relative">
                <!-- Placeholder before script loads -->
                <div id="chat-placeholder" class="absolute inset-0 flex flex-col items-center justify-center text-gray-500 z-0">
                    <div class="w-16 h-16 bg-electric/10 border border-electric/30 rounded-2xl flex items-center justify-center mb-4">
                        <svg class="w-8 h-8 text-electric animate-pulse" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5"><path stroke-linecap="round" stroke-linejoin="round" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
                    </div>
                    <p class="text-sm font-medium">Connecting to Atlas Gateway...</p>
                </div>
            </div>
        </div>
    </section>"""

content = content.replace(old_section, new_section)

with open('/home/james/atlas/website/index.html', 'w') as f:
    f.write(content)

