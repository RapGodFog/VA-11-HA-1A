import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random

# Загружаем переменные окружения из .env файла
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user}[:-5] установленна (◕‿◕✿) ")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def pleaseDie(ctx):
    await ctx.send("I`m dying... urgkh..")
    await bot.close()

@bot.command()
async def roll(ctx):
    await ctx.send(random.randint(0, 100))

@bot.command()
async def game(ctx):
    await ctx.send(random.choice(["rock", "paper", "scisors"]))


# Используем токен из переменных окружения
bot.run(os.getenv('DISCORD_TOKEN'))