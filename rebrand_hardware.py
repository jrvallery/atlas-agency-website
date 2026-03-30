import glob

replacements = {
    # index.html
    "Data stays on your hardware": "Securely hosted OpenClaw agents",
    "Your customer conversations and business data never leave your hardware. No OpenAI, no Google — just you.": "We deploy and manage secure OpenClaw environments for your company. You get the power of advanced AI automation with dedicated cloud infrastructure.",
    "We handle the hardware, the model, and the integration.": "We handle the hosting, the agents, and the integration.",
    "We install and configure on your hardware or secure local server.": "We configure and manage your dedicated cloud-hosted agents.",
    "Local Colorado team": "Colorado-based support",
    "Built for Colorado": "Designed for Scale",
    "We're locals. We understand the Colorado market, its health-conscious culture, and what your customers actually expect.": "We build dedicated AI automation systems and OpenClaw co-pilots tailored exactly to your company's workflows and operational needs.",
    
    # pricing.html
    "Hardware included (or cloud-local hybrid)": "Dedicated Cloud Hosting included",
    "What hardware do I need?": "Do I need any special hardware?",
    "For the AIaaS plan, we handle the hardware — it's included in the monthly fee. For Starter Setup, we'll assess your needs and recommend a compact server (often a refurbished workstation running ~$300–800). We handle sourcing and configuration.": "None. We handle all hosting and infrastructure in the cloud. We deploy OpenClaw agents on dedicated virtual machines specifically provisioned for your company, ensuring maximum uptime and security without any local footprint required.",
    
    # services.html
    "Private LLM on your hardware": "Dedicated OpenClaw Deployments",
    "On-premise LLMs": "Hosted OpenClaw Agents",
    "We build completely private AI models that live on your own physical servers.": "We manage fully capable AI co-pilots deployed on dedicated, secure cloud instances for your business.",
    "Colorado-based team means we can actually show up.": "We provide robust support for your dedicated OpenClaw agents to ensure uninterrupted automation."
}

files = glob.glob('/home/james/atlas/website/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(filepath, 'w') as f:
        f.write(content)
        
print("Hardware/hosting scope updates applied.")
