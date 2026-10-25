
import os
import asyncio
from micup.client import Bot

token = os.environ.get("MICUP_BOT_TOKEN")
bot = Bot()

@bot.on("ready")
async def hazir(b):
    print("Bağlandı:", b.user.username)
    await asyncio.sleep(2)
    await b.set_presence("online")
    print("Presence ayarlandı: online")

@bot.command("!ping")
async def ping(msg):
    return "pong"

bot.run()
