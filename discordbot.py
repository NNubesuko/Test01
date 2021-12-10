import discord
import os
import pprint
from dotenv import load_dotenv
from pathlib import Path
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

load_dotenv()
TOKEN = os.environ['TOKEN']
USER_URL = os.environ['USER_URL']
API_URL = os.environ['API_URL']
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
PRIVATE_KEY = os.environ['PRIVATE_KEY']

bot = commands.Bot(command_prefix="!")
rootPath = Path(__file__).parent

@bot.command()
async def test(ctx):
    print("Hello test command")
    await ctx.channel.send("Hello")

@bot.command()
async def webHandler(ctx):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.youtube.com/')
    content = driver.find_element(By.XPATH, '//*[@id="video-title"]').text
    driver.quit()
    print(content)
    await ctx.channel.send(content)

bot.run(TOKEN)