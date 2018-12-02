import discord


import asyncio
from discord.ext.commands import bot
from discord.ext import commands
import platform
import time
import os
import logging
import youtube_dl
print('=========================================')
print('#Information: ')
logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
	print('============================================================================')
	print ('bot is online.')
	print('bot is running as ' + bot.user.name+',''with the ID:' + bot.user.id+' and connected in '+str(len(bot.servers))+' servers.'' bot is connected with '+str(len(set(bot.get_all_members())))+' members')
	
#Common Messages


    
Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)


msg=('==>')

#===========================
#for my reference
#await client.send_message(message.channel, embed=embed)	
#============================		
			

					
#say command
@bot.command(pass_context = True)
async def say(ctx, *, msg = None):
    await bot.delete_message(ctx.message)

    if not msg: await bot.say("Please specify a message to send")
    else: await bot.say(msg)
    return
    
    															
    																																													
#kick command.        
@bot.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def kick(ctx,user:discord.Member):
	
    if ctx.message.author.server_permissions.kick_members: 
       
        
        await bot.delete_message(ctx.message)
   
        
    try:
        await bot.kick(user) 
        await bot.say(user.name+' was kicked✅  Good bye '+user.name+'!')
	 
    except discord.Forbidden:
        await bot.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await bot.say('kick failed.')
        return		 	


#clear command
@bot.command(pass_context = True)
@commands.has_permissions(manage_messages=True)  
async def clear(ctx, number):

    if ctx.message.author.server_permissions.ban_members: 
         mgs = [] #Empty list to put all the messages in the log
         number = int(number) #Converting the amount of messages to delete to an integer
    async for x in bot.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)             
        
    try:
        await bot.delete_messages(mgs)          
        await bot.say(str(number)+' messages deleted')
	 
    except discord.Forbidden:
        await bot.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await bot.say('clear failed.')
        return			
	

    await bot.delete_messages(mgs)   	

	#mute command	
@bot.command(pass_context=True)
    
@commands.has_permissions(mute_members=True)      

async def mute(ctx,user:discord.Member):
    if ctx.message.author.server_permissions.mute_members: 
             
       role = discord.utils.get(ctx.message.server.roles,name='Muted')
       await bot.delete_message(ctx.message)        
    try:
        await bot.add_roles(ctx.message.mentions[0], role)	 		
        await bot.say('Muted ✅ '+user.name+' 🔇')
          
	 
    except discord.Forbidden:
        await bot.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await bot.say('mute failed.')
        return    	


	  
#unmute command
@bot.command(pass_context=True)
    
@commands.has_permissions(mute_members=True)      

async def vocal(ctx,user:discord.Member):
    if ctx.message.author.server_permissions.mute_members: 
             
       role = discord.utils.get(ctx.message.server.roles,name='Muted')
       await bot.delete_message(ctx.message)        
    try:
        await bot.remove_roles(ctx.message.mentions[0], role)	 		
        await bot.say(' ✅ '+user.name+' 🔉 is now Vocal')
	 
    except discord.Forbidden:
        await bot.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await bot.say('Failed to make Vocal.')
        return        	

    	 		

	  
#ban command	  	  	  
@bot.command(pass_context=True)  
@commands.has_permissions(ban_members=True)      
async def ban(ctx,user:discord.Member):
	
    if ctx.message.author.server_permissions.ban_members: 
         await bot.delete_message(ctx.message)  
        
    try:
        await bot.ban(user)
        await bot.say(user.name+' was banned ✅  Good bye '+user.name+'!')
	 
    except discord.Forbidden:
        await bot.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await bot.say('ban failed.')
        return		 
	   
	
#unban command

@bot.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     

		      	 		 		      	 		 		      	 		 		      	 		 		
async def unban(ctx):
    ban_list = await bot.get_bans(ctx.message.server)

    # Show banned users
    await bot.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

    # Unban last banned user
    if not ban_list:
    	
        await bot.say('Ban list is empty.')
        return
    try:
        await bot.unban(ctx.message.server, ban_list[-1])
        await bot.say('Unbanned user: `{}`'.format(ban_list[-1].name))
    except discord.Forbidden:
        await bot.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await bot.say('unban failed.')
        return
#getbans command

@bot.command(pass_context=True)  
@commands.has_permissions(ban_members=True)		 		      	 		 		
async def bans(ctx):
    ban_list = await bot.get_bans(ctx.message.server)

    # Show banned users
    await bot.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

    
    if not ban_list:
    	
        await bot.say('Ban list is empty.')
        return 
#join command

@bot.command(pass_context=True)
async def join(ctx):
	
	
    if ctx.message.author.server_permissions.kick_members:
        author=ctx.message.author
        vc=author.voice_channel  
    try:	
    	
    	await bot.join_voice_channel(vc)
    	await bot.say('✅connected to voice channel')
    	return
	 
    except discord.Forbidden:
        await bot.say(embed=Forbidden)
        return
    except discord.InvalidArgument:
        await bot.say('Please join voice channel to hear music ')
        return
    except discord.HTTPException:
        await bot.say('join failed.')
        return		 	


#leave command

@bot.command(pass_context=True)
async def leave(ctx):
    if ctx.message.author.server_permissions.kick_members:
        author=ctx.message.author
        vc=author.voice_channel  
    try:
    	await bot.say('✅Disconnecting from voice channel in 8 sec ')
    	await bot.join_voice_channel(vc)
    	await voice_client.disconnect()
    	return
	 
    except discord.Forbidden:
        await bot.say(embed=Forbidden)
        return
    except discord.InvalidArgument:
        await bot.say('Please join voice channel to hear music')
        return
    except discord.HTTPException:
        await bot.say('leave failed.')
        return		 


    

bot.run(os.getenv('Token'))
