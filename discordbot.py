import discord
import os
import pprint
from dotenv import load_dotenv
from pathlib import Path
from discord.ext import commands

load_dotenv()
TOKEN = os.environ['TOKEN']

bot = commands.Bot(command_prefix="!")
rootPath = Path(__file__).parent

@bot.event
async def on_read():
    print(">>>Discordbot has been activated.")

@bot.command()
async def test(ctx):
    await ctx.channel.send("Hello")

bot.run(TOKEN)