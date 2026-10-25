import os
import micup

# Token kontrolü
token = os.getenv("MICUP_BOT_TOKEN")

if not token:
    raise SystemExit("❌ MICUP_BOT_TOKEN bulunamadı!")

# Doğru sınıf / fonksiyon çağrısı (küçük harf veya kütüphanenin yapısına göre)
client = micup.client() # veya kütüphane yapısına göre nesne oluşturma

@client.event
async def on_ready():
    print(f"✅ Bot başarıyla giriş yaptı!")

client.run(token)
