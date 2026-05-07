import asyncio
from telethon import TelegramClient, events

# Configuration
api_id = 8447214
api_hash = '9ec5782ddd935f7e2763e5e49a590c0d'
target_bot_id = 8015674697

client = TelegramClient('session_name', api_id, api_hash)

print('''
       BHOT MEHNAT LAGI HAI BHAMYA EDIT MAT KRNA CODE
       SHOURYA
''')

@client.on(events.NewMessage(from_users=target_bot_id))
async def handle_messages(event):
    # Condition 1: Handle Encounter Buttons
    if "❰ 𝗘 𝗡 𝗖 𝗢 𝗨 𝗡 𝗧 𝗘 𝗥 𝗘 𝗗 ❱" in event.raw_text:
        if event.buttons:
            await event.click(0, 0)
            print("Clicked encounter button.")

    # Condition 2: Handle Victory or Defeat
    elif "🏆 𝗩𝗜𝗖𝗧𝗢𝗥𝗬" in event.raw_text or "💀 𝗗𝗘𝗙𝗘𝗔𝗧" in event.raw_text:
        await event.respond("/explore")
        print("Outcome detected! Sent /explore.")

async def main():
    await client.start()
    print("Client is running...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
