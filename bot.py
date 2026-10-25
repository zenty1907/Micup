from micup import Bot

bot = Bot(ignored_events=["TYPING_START"])

@bot.on("ready")
async def hazir(b):
    print("Bağlandı:", b.user.username)
    await b.set_presence("online")

@bot.command("!ping")
async def ping(msg):
    return "pong"

bot.run()
