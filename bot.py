import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random
import csv

# Загружаем переменные окружения из .env файла
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} установленна (◕‿◕✿) ")

@bot.command()
async def привет(ctx):
    await ctx.send("pong")

# Загрузка запрещенных слов из CSV файла
forbidden_words = []
try:
    with open('filter.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Проверяем, что строка не пустая
                forbidden_words.extend(row)
    print(f"Загружено {len(forbidden_words)} запрещенных слов")
    #print(forbidden_words)
except FileNotFoundError:
    print("Внимание: файл filter.csv не найден!")
except Exception as e:
    print(f"Ошибка при чтении файла filter.csv: {e}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if any(word in message.content.lower() for word in forbidden_words):
        await message.delete()
        await message.channel.send(f"{message.author.mention}, ваше сообщение было удалено из-за использования запрещенных слов.")
    
    await bot.process_commands(message)


@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='полигон')  # Замените 'general' на имя вашего канала
    if channel:
        await channel.send(f"Привет, {member.mention}! Добро пожаловать на сервер!")

@bot.event
async def on_ready():
    channel = discord.utils.get(bot.guilds[0].text_channels, name='полигон')  # Замените 'general' на имя вашего канала
    if channel:
        await channel.send(f"Аллах возроди \nПривет всем! Я {bot.user.name}, рада вас видеть! (◕‿◕✿)")

@bot.command()
async def спасибо(ctx):
    await ctx.send("Всегда пожалуйста! (◕‿◕✿)")

@bot.command()
async def brexit(ctx):
    await ctx.send("-1")
    await bot.close()

@bot.command()
async def roll(ctx):
    await ctx.send(random.randint(0, 100))

@bot.command()
async def game(ctx):
    await ctx.send(random.choice(["rock", "paper", "scisors"]))

bot.run(os.getenv('DISCORD_TOKEN'))