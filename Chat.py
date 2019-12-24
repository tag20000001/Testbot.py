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
	if message.author == bot.user:
		return
	if message.author == Client.user:
		return
	if message.author == Bot.user:
		return
	elif message.content.startswith(','):
		return
	elif message.content.startswith('.'):
		return
	elif message.content.startswith('!'):
		return
	elif message.content.startswith('+'):
		return
	elif message.content.startswith('×'):
		return
	elif message.content.startswith('÷'):
		return
	elif message.content.startswith('='):
		return
	elif message.content.startswith('/'):
		return
	elif message.content.startswith('_'):
		return
	elif message.content.startswith('$'):
		return
	elif message.content.startswith('%'):
		return
	elif message.content.startswith('&'):
		return
	elif message.content.startswith('-'):
		return
	elif message.content.startswith('"'):
		return
	elif message.content.startswith('*'):
		return
	elif message.content.startswith(':'):
		return
	elif message.content.startswith(':'):
		return
	elif message.content.startswith(';'):
		return
	elif message.content.startswith('?'):
		return
	elif message.content.startswith('p!'):
		return
	elif message.content.startswith('mv!'):
		return
	elif message.content.startswith('h!'):
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
	elif 'Gm' in message.content or 'gm' in message.content or'Good Morning' in message.content or 'good morning' in message.content:
		msg = await  message.channel.send(embed=discord.Embed(title="Good Morning"+user,color=0x00ff00))
		return
	elif 'Gn' in message.content or 'gn' in message.content or'Good Night' in message.content or 'good night' in message.content:
		msg = await  message.channel.send(embed=discord.Embed(title="Good Night"+user,color=0x00ff00))
		return
	elif 'Good Evening' in message.content or 'Good evening' in message.content or 'good evening' in message.content or 'GOOD EVENING' in message.content or 'good Evening' in message.content or '' in message.content or 'Good Evening <@556485152486981642>'  in message.content or '<@556485152486981642>good evening' in message.content or '<@556485152486981642>Good Evening'  in message.content  or '<@556485152486981642> good evening' in message.content or '<@556485152486981642>GOOD EVENING'  in message.content:
		msg = await  message.channel.send(embed=discord.Embed(title="Good Evening"+user,color=0x00ff00))
		return
	elif 'Not fine' in message.content or 'not fine' in message.content or 'Not well' in message.content or 'not well' in message.content or 'Not good' in message.content or 'not good' in message.content or 'tired' in message.content or 'Tired' in message.content or 'sick' in message.content or 'Sick' in message.content:
		await message.add_reaction('😔')
		return

	
	elif 'fine' in message.content or 'Fine' in message.content or 'well' in message.content or 'Well' in message.content or 'good' in message.content or 'Good' in message.content:
		await message.add_reaction('👍')
		return
	
	await client.process_commands(message)
	
#Shut down command
@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)
async def turnoffchat(ctx):
	msg="chat is turned off\nBye:ballot_box_with_check: "
	msg_embed=discord.Embed(title="Turning off...", description=msg,color=0x00ff00)
	await ctx.send(embed=msg_embed)
	await client.close()
	return
	
	
client.run(os.getenv('Token'))
  
		
