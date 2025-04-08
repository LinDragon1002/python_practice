import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
APPLICATION_ID = os.getenv("APPLICATION_ID")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents, application_id=APPLICATION_ID)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'成功啟用\n已開啟 {bot.user}')

# 📌 自動載入 Cogs
async def load_cogs():
    for filename in os.listdir("./Cogs"):
        if filename.endswith(".py") and filename == "SlahCommand.py":
            await bot.load_extension(f"Cogs.{filename[:-3]}")  # 移除 `.py`

# 📌 啟動 Bot
async def main():
    await load_cogs()
    await bot.start(TOKEN) # type: ignore

import asyncio
asyncio.run(main())