import os
import micup

token = os.getenv("MICUP_BOT_TOKEN")

if not token:
    raise SystemExit("❌ MICUP_BOT_TOKEN bulunamadı!")

# Doğru sınıf olan 'Bot' sınıfını kullanıyoruz
bot = micup.Bot()

@bot.event
async def on_ready():
    print(f"✅ Bot başarıyla giriş yaptı!")

bot.run(token)
