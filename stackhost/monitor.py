import asyncio
from runner import running, start_bot
from database import bots

async def monitor_bots():
    while True:

        async for bot in bots.find({"status":"running"}):
            bot_id = bot["bot_id"]

            process = running.get(bot_id)

            if not process or process.poll() is not None:
                start_bot(bot["path"], bot_id)

        await asyncio.sleep(20)
