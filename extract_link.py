from telethon import TelegramClient
import asyncio
import re

# Telegram API credentials
api_id = "API ID TELEGRAM" # ← Your actual API ID
api_hash = 'API HASH TELEGRAM'
phone = '+98********'  # ← Your phone number including country code

# Output file path
output_file = "saved_links.txt"

client = TelegramClient("extract_links_session", api_id, api_hash)

async def extract_links():
    await client.start(phone)
    print("✅ Logged in successfully")

    all_links = []
    seen_links = set()

    # Iterate over saved messages (from oldest to newest)
    async for msg in client.iter_messages("me", reverse=True):
        if msg.message:
            # Extract direct links from message text
            text_links = re.findall(r'https://t\.me/[^\s"\']+', msg.message)
            for link in text_links:
                if link not in seen_links:
                    all_links.append(link)
                    seen_links.add(link)

            # Extract hidden hyperlinks (e.g. inside buttons or rich text)
            if msg.entities:
                for entity in msg.entities:
                    if hasattr(entity, 'url') and entity.url:
                        if entity.url not in seen_links:
                            all_links.append(entity.url)
                            seen_links.add(entity.url)

    # Save the links to a text file
    with open(output_file, "w", encoding="utf-8") as f:
        for link in all_links:
            f.write(link + "\n")

    print(f"🔗 {len(all_links)} links extracted and saved to: {output_file}")

# Run the async function
asyncio.run(extract_links())
