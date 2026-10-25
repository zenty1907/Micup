import os
import micup

token = os.environ.get("MICUP_BOT_TOKEN")

if not token:
    raise SystemExit("❌ MICUP_BOT_TOKEN bulunamadı! Secrets kısmını kontrol et.")

client = micup.Client()

@client.event
async def on_ready():
    print(f"✅ Giriş yapıldı: {client.user}")

client.run(token)
