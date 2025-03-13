import requests
import time
import random
import os

# Get webhook URLs from Render environment variables
WEBHOOKS = [
    os.getenv("WEBHOOK1"),
    os.getenv("WEBHOOK2"),
    os.getenv("WEBHOOK3"),
    os.getenv("WEBHOOK4"),
    os.getenv("WEBHOOK5")
]

# Messages to send (Natural & Engaging)
MESSAGES = [
    "**🔥 W H A T ' S   Y O U R   F A V O R I T E   P O K É M O N ? 🔥**",
    "__⚡ W H O O O ' S   S T R O N G E R R R :   P I K A C H U U U U   O R   C H A R I Z A R D D D ? ⚡__",
    "**💎 I   H O P E   A   R A R E E E E   P O K É M O N   S P A W N S   S O O O O N ! 💎**",
    "__🎯 G U E S S S S   T H E   N E X T   P O K É M O N   T O   A P P E A R R R ! 🎯__",
    "**🌀 A N Y O N E   L U C K Y   E N O U G H   T O   F I N D   A   S H I N Y ? ✨**",
]

def send_message():
    webhook = random.choice(WEBHOOKS)  # Pick a random webhook
    message = random.choice(MESSAGES)  # Pick a random message
    if webhook:
        requests.post(webhook, json={"content": message})  # Send message
        print(f"✅ Sent message: {message}")
    else:
        print("⚠️ Webhook URL missing!")

while True:
    send_message()
    time.sleep(random.randint(20, 60))  # Random wait time (20-60 sec)
