import discord
import asyncio
from discord.ext.commands import bot
from discord.ext import commands
import platform
import os
import time


	
#Common Messages





    
Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)

@bot.command(pass_context=True)
async def join(ctx):
	author=ctx.message.author
	vc=author.voice_channel
	await bot.join_voice_channel(vc)
	return
	
@bot.command(pass_context=True)
async def leave(ctx):
	author=ctx.message.author
	vc=author.voice_channel
	await bot.disconnect()
	return
	
@bot.command(pass_context=True)
async def shutdown(ctx):
	await bot.close()
	return


    	



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    user='{0.author}'.format(message)
    hlo = 'Hello!  {0.author}'.format(message)
    
   

    if message.content.startswith('Hi'):
    	await bot.send_message(message.channel,embed=discord.Embed(title='Hello '+user,color=0x00ff00))
    if message.content.startswith('Hello'):
    	await bot.send_message(message.channel,embed=discord.Embed(title='Hello '+user,color=0x00ff00))    	    	
		
		




