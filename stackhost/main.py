from pyrogram import Client, filters
from config import *
from runner import clone_repo, install_requirements, start_bot, stop_bot
from database import bots

app = Client(
    "StackHostBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply(
        "✅ StackHostBot Ready\nSend:\n/host <github_repo>"
    )


# HOST BOT FROM GITHUB
@app.on_message(filters.command("host"))
async def host(_, message):

    if len(message.command) < 2:
        return await message.reply("Send GitHub repo link.")

    repo = message.command[1]
    user_id = message.from_user.id

    await message.reply("⬇️ Cloning repo...")

    path = clone_repo(repo, user_id)

    await message.reply("📦 Installing requirements...")
    install_requirements(path)

    await message.reply("🚀 Starting bot...")
    pid = start_bot(path, user_id)

    await bots.insert_one({
        "user_id": user_id,
        "repo": repo,
        "path": path,
        "pid": pid,
        "status": "running"
    })

    await message.reply("✅ Bot Hosted Successfully!")


# STOP BOT
@app.on_message(filters.command("stop"))
async def stop(_, message):
    user_id = message.from_user.id

    stop_bot(user_id)

    await bots.update_one(
        {"user_id": user_id},
        {"$set": {"status": "stopped"}}
    )

    await message.reply("🛑 Bot stopped.")


app.run()
