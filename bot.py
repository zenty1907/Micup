import os
import micup

# Token bilgisini ortam değişkeninden (Secrets) alıyoruz
token = os.getenv("MICUP_BOT_TOKEN")

if not token:
    raise SystemExit("❌ MICUP_BOT_TOKEN bulunamadı! GitHub Secrets kısmına token'ını eklediğinden emin ol.")

# Micup Client başlatma
client = micup.Client()

@client.event
async def on_ready():
    print(f"✅ Giriş yapıldı! Bot Kullanıcı Adı: {client.user.name}")

@client.event
async def on_message(message):
    # Botun kendi mesajlarına yanıt vermesini engelle
    if message.author.bot:
        return
    
    # Basit bir test komutu
    if message.content == "!merhaba":
        await message.channel.send(f"Selam {message.author.name}, bot aktif! 🚀")

# Botu çalıştır
client.run(token)
