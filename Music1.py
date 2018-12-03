import discord
import random
import asyncio
from discord.ext.commands import bot
from discord.ext import commands
import platform
import time
import os
import logging
print('=========================================')
print('Music.py is on')
bot = commands.Bot(command_prefix='.')

#join command
@bot.command(pass_context=True)
async def join(ctx):
    if ctx.message.author.server_permissions.kick_members:
        author=ctx.message.author
        vc=author.voice_channel  
    try:
    	
    	msg= await bot.send_message(ctx.message.channel,'✅connecting to voice channel')
    	
    	await asyncio.sleep(2)
    	await bot.delete_message(msg)
    	await bot.delete_message(ctx.message)	
    	
    	await bot.join_voice_channel(vc)
    	
    	return
	 
    except discord.Forbidden:
        await bot.say(embed=Forbidden)
        return
    except discord.InvalidArgument:
        msg2=await bot.send_message(ctx.message.channel,'Please join a voice channel to hear music')
        await asyncio.sleep(2)
        await bot.delete_message(msg2)
        return
    except discord.HTTPException:
        await bot.say('join failed.')
        return		 	


		

#Leave command
@bot.command(pass_context=True)
async def leave(ctx):
    if ctx.message.author.server_permissions.kick_members:
        author=ctx.message.author
        server=ctx.message.server
        vc=author.voice_channel
        voice_client=bot.voice_client_in(server) 
    try:
    	msg=await bot.send_message(ctx.message.channel,'✅Disconnecting from voice channel in 8 sec ')
    	await asyncio.sleep(2)
    	await bot.delete_message(msg)
    	await bot.delete_message(ctx.message)
    	await bot.join_voice_channel(vc)	
    	return
	 
    except discord.Forbidden:
        await bot.say(embed=Forbidden)
        return
    except discord.InvalidArgument:
        msg2= await bot.send_message(ctx.message.channel,'Please join a voice channel to hear music')
        await asyncio.sleep(2)
        await bot.delete_message(msg2)
        return
    except discord.HTTPException:
        await bot.say('leave failed.')
        return		

bot.run(os.getenv('Token'))
