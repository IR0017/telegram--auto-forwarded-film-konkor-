from telethon import TelegramClient
import asyncio
import time
import random
import re
import os

# account information
api_id = 'API ID TELEGRAM'  # ← API ID 
api_hash = 'API HASH TELEGRAM'  # ← API HASH 
phone = '+98********'  # ← phone number

# oringin bot lit to forwareded
bot_links = [
    "ORIGIN BOT LINKS"
]





# destinition channel id to forwarded
target_channel = ''  # "https://t.me/your_channel

# Sent message ID file
forwarded_ids_file = "forwarded_ids.txt"

client = TelegramClient('forward_bot', api_id, api_hash)

def load_forwarded_ids():
    if not os.path.exists(forwarded_ids_file):
        return set()
    with open(forwarded_ids_file, "r") as f:
        return set(line.strip() for line in f.readlines())

def save_forwarded_id(msg_id):
    with open(forwarded_ids_file, "a") as f:
        f.write(str(msg_id) + "\n")

async def forward_files_from_bot(link):
    try:
        print(f'\n▶️ Processing link: {link}')
        
        bot_username = re.search(r'https?://t\.me/([^?]+)', link).group(1)
        start_param_match = re.search(r'start=([^&]+)', link)
        start_param = start_param_match.group(1) if start_param_match else ''
        
        start_command = f'/start {start_param}' if start_param else '/start'
        await client.send_message(bot_username, start_command)
        print(f'🟢 Sent "{start_command}" to {bot_username}')
        
        await asyncio.sleep(5)
        
        messages = await client.get_messages(bot_username, limit=20)
        forwarded_ids = load_forwarded_ids()
        file_found = False
        
        for msg in reversed(messages):  # to maintain original order
            if msg.media and str(msg.id) not in forwarded_ids:
                await msg.forward_to(target_channel)
                print(f"📁 File forwarded. Message ID: {msg.id}")
                save_forwarded_id(msg.id)
                file_found = True
                time.sleep(2)
        
        if not file_found:
            print("⚠️ No new files found in recent messages from the bot.")
    except Exception as e:
        print(f'❌ Error processing {link}: {e}')

async def main():
    await client.start(phone)
    print("✅ Logged in successfully.")

    for index, link in enumerate(bot_links):
        await forward_files_from_bot(link)

        if index < len(bot_links) - 1:
            delay = random.randint(8, 15)
            print(f"⏳ Waiting {delay} seconds before next link...")
            await asyncio.sleep(delay)

    print("\n🏁 All links processed.")

asyncio.run(main())
