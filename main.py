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
wikipedia.set_lang("pt-br")

@bot.event
async def on_ready():
     print("""
Status: Online
Author: Davi Bassani
Pertence a: Dev Server BR
Nome: Dev Server Bot
""")
           
@bot.command()
async def hello(ctx):
    await ctx.send(f"Olá, {ctx.author.name}!")

@bot.command()
async def horas(ctx):
    await ctx.send(f"Agora são {time.strftime('%H:%M')}")

@bot.command()
async def wiki(ctx, arg):
    busca = wikipedia.search(arg)
    await ctx.send(f"{str(busca)}")

bot.run(token)