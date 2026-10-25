import os
from micup.client import Bot

token = os.environ.get("MICUP_BOT_TOKEN")
bot = Bot()

@bot.event
async def on_ready():
    print(f"✅ Giriş yapıldı: {bot.user}")

bot.run(token)
