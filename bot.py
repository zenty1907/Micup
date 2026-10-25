import micup

bot = micup.Bot("1563866366481006596.CNMf87xHJ8dxCGL3VoAS7HGCUvVZWfmqt0W-SLo81Hk")

@bot.event
async def on_message(message):
    # Kendi kendine yanıt vermemesi için
    if message.author == bot.user:
        return
    
    # Eğer biri sohbette "!selam" yazarsa bot yanıt versin
    if message.content == "!selam":
        await message.channel.send("Aleykümselam! Bot aktif ve çalışıyor 🚀")

bot.run()
