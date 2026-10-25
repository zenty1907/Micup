import micup

bot = micup.Bot("1563866366481006596.CNMf87xHJ8dxCGL3VoAS7HGCUvVZWfmqt0W-SLo81Hk")

@bot.event
async def on_ready():
    print(f"Bot aktif: {bot.user.name}")
    # Botun durumunu çevrim içi yapmak veya etkinlik ayarlamak için
    await bot.change_presence(status="online", activity="Zentyy Yayınları")

bot.run()
