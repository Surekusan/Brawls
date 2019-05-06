import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = ".")
@client.event
async def on_ready():
    print("Danke das du den Brawl Zone Bot verwendest")
    await client.change_presence(game=discord.Game(name=".help"))

@client.event
async def on_message(message):
    if message.content.startswith('.Hi'):
        msg = 'Hi {0.author.mention}' .format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('.test'):
        msg = 'tete {0.author.mention}' .format(message)
        await client.send_message(message.channel, msg)

client.run(os.getenv('TOKEN'))

                    
