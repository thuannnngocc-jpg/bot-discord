import discord
import os
TOKEN = os.getenv('TOKEN')  # Token của bạn
LINK = "tất cả file định vị,aim,proxy,fake lag,menu,mod skin tại đây: https://beacons.ai/thuannngocc"  # Link bạn muốn gửi (thay link thật vào)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Bot đã online: {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if "link" in message.content.lower() or "file" in message.content.lower():
        await message.channel.send(f"🔗 Link: {LINK}")

client.run(TOKEN)