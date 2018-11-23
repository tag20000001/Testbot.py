import discord
import random
import asyncio
from discord.ext.commands import bot
from discord.ext import commands
import platform
import time
import os
@bot.event
async def on_ready():
	print("chat.py is on")
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    user='{0.author.name}'.format(message)
    hlo ='Hello!  {0.author}'.format(message)
    greetmsg=["Hi ","Hello ","Hey ","Yo "]
    usergreet=["Hi" or "Hello" or "Hey" or "Yo"]
    
    if message.content.startswith("."):
    	return
     

    if message.content.startswith("Hi")or message.content.startswith("Hello")or message.content.startswith("Hey")or message.content.startswith("Yo")or message.content.endswith("Hi")or message.content.endswith("Hello")or message.content.endswith("Hey")or message.content.endswith("Yo")or message.content.startswith("hi")or message.content.startswith("hello")or message.content.startswith("hey")or message.content.startswith("yo")or message.content.endswith("hi")or message.content.endswith("hello")or message.content.endswith("hey")or message.content.endswith("yo"):
    	await bot.send_message(message.channel,embed=discord.Embed(title=random.choice(greetmsg)+user,color=0x00ff00))
    if message.content.startswith('Bye')or message.content.startswith("bye")or message.content.endswith("Bye")or message.content.endswith("bye"):
    	await bot.send_message(message.channel,embed=discord.Embed(title='Bye '+user,color=0x00ff00))    	    	

bot.run(os.getenv('Token'))
		
