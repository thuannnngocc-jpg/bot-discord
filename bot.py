import os
import discord
from keep_alive import keep_alive

keep_alive()

TOKEN = os.getenv("TOKEN")

LINK = "tất cả file định vị, aim, proxy, fake lag, menu, mod skin tại đây: https://beacons.ai/thuannngocc"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot đã online: {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    if "link" in msg or "file" in msg:
        await message.channel.send(f"🔗 {LINK}")

client.run(TOKEN)