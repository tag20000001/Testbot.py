import discord
import random
import asyncio
from discord.ext.commands import bot
from discord.ext import commands
from discord.utils import get
import platform
import time
import os
import logging
print('=========================================')
print('#Information: ')
logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
	print('=========================================')
	print('advchat.py is on')

#new improved chat
@bot.event
async def on_message(message):
	user='{0.author.name}'.format(message)
	greetmsg=["Hi ","Hello ","Hey ","Yo "]
	msg3=['Bye ','Bye for now ']
	msghru=['Fine and what about you ','Felling well :D and what about you ','Good and what about you ']
	emj=[':ok_hand:',':thumbsup:']
	if message.author is bot.user:
		return
	elif message.content.startswith("."):
		return
	elif 'hi' in message.content or 'hello' in message.content or 'yo <@450220085676605441>' in message.content or 'hey' in message.content or 'Hi' in message.content or 'Hello' in message.content or 'Yo <@450220085676605441>'  in message.content or '<@450220085676605441>Yo' in message.content or '<@450220085676605441>yo'  in message.content  or '<@450220085676605441> Yo' in message.content or '<@450220085676605441> yo'  in message.content  or 'Hey' in message.content:
		msg = await  bot.send_message(message.channel,embed=discord.Embed(title=random.choice(greetmsg)+user,color=0x00ff00))
		return
		
	elif 'bye' in message.content or 'Bye' in message.content:
		msg = await  bot.send_message(message.channel,embed=discord.Embed(title=random.choice(msg3)+user,color=0x00ff00))
		return		
	elif 'how are you' in message.content or 'How are you' in message.content or 'how r u' in message.content or 'How r u' in message.content:
		msg = await  bot.send_message(message.channel,embed=discord.Embed(title=random.choice(msghru)+user+'? ',color=0x00ff00))
		return
	elif 'Not fine' in message.content or 'not fine' in message.content or 'Not well' in message.content or 'not well' in message.content or 'Not good' in message.content or 'not good' in message.content or 'tired' in message.content or 'Tired' in message.content or 'sick' in message.content or 'Sick' in message.content:
		await bot.add_reaction(message,'😔')
		return

	
	elif 'fine' in message.content or 'Fine' in message.content or 'well' in message.content or 'Well' in message.content or 'good' in message.content or 'Good' in message.content:
		await bot.add_reaction(message,'👍')
		return
	

    
bot.run(os.getenv('Token'))  
    	  	

	

    

 
    	  	
