'''
pip install discord.py
'''
import discord
from discord.ext import commands
import secret
import time
import wikipedia

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

token = secret.TOKEN()
wikipedia.set_lang("pt")

@bot.event
async def on_ready():
     print("""
Status: Online
Author: Davi Bassani
Pertence a: Dev Server BR
Nome: Dev Server Bot
""")
           
@bot.command()
async def hello(message):
    await message.send(f"Olá, {message.author.name}!")

@bot.command()
async def horas(message):
    await message.send(f"Agora são {time.strftime('%H:%M')}")

@bot.command()
async def search(message, arg):
    busca = wikipedia.search(arg)
    await message.send(f"{busca}")

@bot.command()
async def summary(message, arg):
    busca = wikipedia.summary(arg)
    try: 
        await message.send(f"{busca}")
    except Exception as e:
        await message.send(f'Ocorreu o seguinte erro: {e}')

@bot.command()
async def page(message, arg):
    busca = wikipedia.page(arg)
    try: 
        await message.send(f"{busca}")
    except Exception as e:
        await message.send(f'Ocorreu o seguinte erro: {e}')

bot.run(token)