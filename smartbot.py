import discord
import asyncio
import random
from discord.ext.commands import bot
from discord.ext import commands
from discord.voice_client import VoiceClient
import time
import logging
import os

import youtube_dl
import ffmpeg
startup_extensions = {"Music"}
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
			
class Main_Commands():
	def _init_(self,bot):
		self.bot=bot
					
#say command
@bot.command(pass_context = True)
async def say(ctx, *, msg = None):
	speech= discord.Embed(title=" ", description=msg,color=0x00ff00)
	await bot.delete_message(ctx.message)
	if not msg: await bot.say("Please specify a message to send")
	else: await bot.say(embed=speech)
	return
    
    
    															
    																																													
#kick command.        
@bot.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def kick(ctx,user:discord.Member):

    if ctx.message.author.server_permissions.kick_members: 
       
        
        await bot.delete_message(ctx.message)
   
        
    try:
        await bot.kick(user)
        msg=user.name+' was kicked ✅  Good bye '+user.name+'!'
        msg_embed=discord.Embed(title="Kicked User <@"+user.id+">", description=msg,color=0x00ff00)
        await bot.say(embed=msg_embed)

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
        a=await bot.say(str(number)+' messages deleted')
        await asyncio.sleep(5)
        await bot.delete_message(a)
    except discord.Forbidden:
        await bot.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await bot.say('clear failed.')
        return			
	

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
#ping command
@bot.command(pass_context = True)
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await bot.send_typing(channel)
    t2 = time.perf_counter()
    await bot.say("Ping: {}ms".format(round((t2-t1)*1000)))
    return

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

	
inv_embed=discord.Embed(title="Invite bot from here", description="Invitation link", color=0x00ff00)
inv_embed.add_field(name="Click here", value="https://discordapp.com/api/oauth2/authorize?client_id=556485152486981642&permissions=8&scope=bot")

#invite command
@bot.command(pass_context=True)
async def invite(ctx):
	await bot.say(embed=inv_embed)
	return
#spam command
@bot.command(pass_context=True)  
@commands.has_permissions(ban_members=True)                                             
async def spam(ctx,number):
	int(number)
	i=1
	t=30*number
	while(i<=int(t)):
		spam_list=['hi','hello','GM','GN','HEY','Spam','Random','A','B','C','Z']
		await asyncio.sleep(2)
		await bot.say(random.choice(spam_list))
		i=i+1
		
#Shut down command
@bot.command(pass_context=True)  
@commands.has_permissions(ban_members=True)
async def shutdown(ctx):
	msg="Shut Down Success. /n Bye"
	msg_embed=discord.Embed(title="Shutting down...", description=msg,color=0x00ff00)
	await bot.say(embed=msg_embed)
	await bot.say(embed=msg_embed)
	await bot.close()
	return
	
	

for extension in startup_extensions:
	try:
		bot.load_extension(extension)
	except Exception as e:
		exc = '{} : {}'.format(type(e),e)
		print('Failed to load extension {}\n{}'.format(extension, exc) )
		
		
		
bot.run(os.getenv('Token'))
				

	
	
