import discord
import os
import sys
import time
import asyncio
import random
import traceback
import tracemalloc
import youtube_dl
from discord.ext import commands
print('=========================================')
print('#Information: ')
client = discord.Client()
client= commands.Bot(command_prefix='.')
@client.event
async def on_ready():
    
    print('============================================================================')
  
    print ('bot is online.')
@client.event
async def on_message(message):
	user='{0.author.name}'.format(message)
	greetmsg=["Hi ","Hello ","Hey ","Yo "]
	byemsg=["Bye for now","See you  ","Bye CYA ","Bye bye "]
	msg3=['Bye ','Bye for now ']
	msghru=['Fine and what about you ','Felling well :D and what about you ','Good and what about you ']
	emj=[':ok_hand:',':thumbsup:']
	if message.author == client.user:
		return
	elif message.content.startswith('.'):
		return
	elif 'hi' in message.content or 'hello' in message.content or 'Yo <@556485152486981642>' in message.content or 'hey' in message.content or 'Hi' in message.content or 'Hello' in message.content or 'Yo <@556485152486981642>'  in message.content or '<@556485152486981642>Yo' in message.content or '<@556485152486981642>yo'  in message.content  or '<@556485152486981642> Yo' in message.content or '<@556485152486981642> yo'  in message.content  or 'Hey' in message.content:
		msg = await  message.channel.send(embed=discord.Embed(title=random.choice(greetmsg)+user,color=0x00ff00))
		return
		
	elif 'bye' in message.content or 'Bye' in message.content:
		msg = await  message.channel.send(embed=discord.Embed(title=random.choice(msg3)+user,color=0x00ff00))
		return		
	elif 'how are you' in message.content or 'How are you' in message.content or 'how r u' in message.content or 'How r u' in message.content:
		msg = await  message.channel.send(embed=discord.Embed(title=random.choice(msghru)+user+'? ',color=0x00ff00))
		return
	elif 'bye' in message.content or 'Bye' in message.content or 'Bye <@556485152486981642>' in message.content or 'BYE' in message.content or 'see you' in message.content or 'See you' in message.content or 'Bye <@556485152486981642>'  in message.content or '<@556485152486981642>Bye' in message.content or '<@556485152486981642>bye'  in message.content  or '<@556485152486981642> Bye' in message.content or '<@556485152486981642> bye'  in message.content:
		msg = await  message.channel.send(embed=discord.Embed(title=random.choice(byemsg)+user,color=0x00ff00))
		return
	elif 'Not fine' in message.content or 'not fine' in message.content or 'Not well' in message.content or 'not well' in message.content or 'Not good' in message.content or 'not good' in message.content or 'tired' in message.content or 'Tired' in message.content or 'sick' in message.content or 'Sick' in message.content:
		await message.add_reaction('😔')
		return

	
	elif 'fine' in message.content or 'Fine' in message.content or 'well' in message.content or 'Well' in message.content or 'good' in message.content or 'Good' in message.content:
		await message.add_reaction('👍')
		return
	
	await client.process_commands(message)
	
	
client.run(os.getenv('Token'))
  
		
