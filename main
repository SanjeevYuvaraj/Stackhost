from pyrogram import Client, filters
from config import *
from runner import *
from database import bots
from monitor import monitor_bots
import asyncio
import uuid

app = Client(
    "StackHost",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@app.on_message(filters.command("start"))
async def start(_, m):
    await m.reply(
        "🔥 PRO StackHostBot\n\n"
        "/host <github>\n"
        "/stop\n/restart\n/logs"
    )


# HOST
@app.on_message(filters.command("host"))
async def host(_, m):

    repo = m.command[1]
    bot_id = str(uuid.uuid4())

    await m.reply("Cloning repo...")

    path = clone_repo(repo, bot_id)
    install_req(path)

    pid = start_bot(path, bot_id)

    await bots.insert_one({
        "bot_id": bot_id,
        "user_id": m.from_user.id,
        "repo": repo,
        "path": path,
        "pid": pid,
        "status": "running"
    })

    await m.reply(f"✅ Hosted!\nBot ID: `{bot_id}`")


# STOP
@app.on_message(filters.command("stop"))
async def stop(_, m):

    bot = await bots.find_one({"user_id":m.from_user.id})

    stop_bot(bot["bot_id"])

    await bots.update_one(
        {"bot_id":bot["bot_id"]},
        {"$set":{"status":"stopped"}}
    )

    await m.reply("🛑 Bot stopped.")


# RESTART
@app.on_message(filters.command("restart"))
async def restart(_, m):

    bot = await bots.find_one({"user_id":m.from_user.id})

    restart_bot(bot["path"], bot["bot_id"])

    await m.reply("♻️ Restarted.")


# LOGS
@app.on_message(filters.command("logs"))
async def logs(_, m):

    bot = await bots.find_one({"user_id":m.from_user.id})

    await m.reply_document(f"logs/{bot['bot_id']}.log")


async def main():
    await app.start()
    asyncio.create_task(monitor_bots())
    await idle()

from pyrogram import idle
asyncio.run(main())
