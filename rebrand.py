import os
import glob
import re

files = glob.glob('/home/james/atlas/website/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # 1. Broad region replacements
    content = content.replace('Boulder, Colorado', 'Colorado')
    content = content.replace('Boulder, CO', 'Colorado')
    content = content.replace('Boulder', 'Colorado')
    content = content.replace('boulder', 'colorado')
    
    # 2. Rebrand Name (if not already "Atlas")
    content = content.replace('Atlas AI', 'Colorado AI Atlas')
    
    # 3. Update core value props to match new scope
    content = content.replace(
        'Colorado AI Atlas builds private, on-premise AI agents that handle your bookings, answer customer questions 24/7, and automate your workflows — without ever sending your data to Big Tech.',
        'Colorado AI Atlas builds, hosts, and manages custom OpenClaw AI agents. We provide fully capable digital co-pilots for your company to automate workflows, scale operations, and deliver 24/7 value without the headache of managing local AI infrastructure.'
    )
    
    content = content.replace(
        'Private AI for Local Businesses',
        'Managed OpenClaw Agents & AI Co-pilots'
    )
    
    content = content.replace(
        'Every Colorado AI Atlas build runs on hardware located at your site (or a Colorado-area private server). No conversation data is ever sent to OpenAI, Google, or any cloud provider. You own it all.',
        'We host and manage dedicated OpenClaw agents for your company on secure cloud infrastructure. This ensures 24/7 uptime, scalable performance, and removes the burden of maintaining complex local hardware, while keeping your data strictly isolated.'
    )
    
    with open(filepath, 'w') as f:
        f.write(content)
        
print("Rebranding and scope update applied.")
