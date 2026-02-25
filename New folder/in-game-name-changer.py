import os
from dotenv import load_dotenv
import discord

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.name == "🍆in-game-name":
        try:
            await message.author.edit(nick=message.content)
            await message.channel.send("✅ Your nickname has been updated!")
        except discord.Forbidden:
            await message.channel.send("❌ I don't have permission to change your nickname.")
        except Exception as e:
            print(e)

client.run(TOKEN)