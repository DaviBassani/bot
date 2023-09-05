'''
pip install discord.py
'''
import discord
from discord.ext import commands
import secret

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

x = 10
y = 1.5
z = "String"


token = secret.TOKEN()

print("""
Author: Davi Bassani
Pertence a: Dev Server BR
Nome: Dev Server Bot
""")
      
bot.run(token)