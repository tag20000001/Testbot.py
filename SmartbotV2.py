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
#from dotenv import load_dotenv
import logging
print('=========================================')
print('#Information: ')

logging.basicConfig(level=logging.INFO)
#load_dotenv()

tracemalloc.start()

client = discord.Client()
client= commands.Bot(command_prefix='.')

#Common Messages


    
Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)

inv_embed=discord.Embed(title="Invite bot from here", description="Invitation link", color=0x00ff00)
inv_embed.add_field(name="Click here", value="https://discordapp.com/api/oauth2/authorize?client_id=556485152486981642&permissions=8&scope=bot")



@client.event
async def on_ready():
    
    print('============================================================================')
    print('We have logged in as {0.user}'.format(client))
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
		
#say command
@client.command(pass_context = True)
async def say(ctx, *, msg = None):
	speech= discord.Embed(title=" ", description=msg,color=0x00ff00)
	await ctx.message.delete()
	if not msg: await ctx.send("Please specify a message to send")
	else: await ctx.send(embed=speech)
	return
	
#kick command.        
@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def kick(ctx,user:discord.Member):
	
	await ctx.message.delete()
	try:
		member=discord.Member
		await user.kick()
		
		msg=user.name+' was kicked ✅  Good bye '+user.name+'!'
		msg_embed=discord.Embed(title="Kicked User <@"+user.name+">", description=msg,color=0x00ff00)
		await ctx.send(embed=msg_embed)
	except discord.Forbidden:
		await ctx.send(embed=Forbidden)
		return
	except discord.HTTPException:
		await ctx.send('kick failed.')
		return	
	
#clear command
@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)  
async def clear(ctx, number):
	
	
	mgs = [] #Empty list to put all the messages in the log
	number = int(number) #Converting the amount of messages to delete to an integer
	
	async for x in ctx.channel.history(limit = number+1):
		mgs.append(x)
	try:
		await ctx.channel.delete_messages(mgs)
		a=await ctx.send(str(number)+' messages deleted')
		await asyncio.sleep(5)
		await a.delete()
	except discord.Forbidden:
		await ctx.send(embed=Forbidden)
		return
	except discord.HTTPException:
		await ctx.send('clear failed.')
		return				 	

#mute command	
@client.command(pass_context=True)
    
@commands.has_permissions(administrator=True)     
async def mute(ctx,user:discord.Member):
	role = discord.utils.get(ctx.guild.roles,name='Muted')
	await ctx.message.delete()
	try:
		await discord.Member.add_roles(ctx.message.mentions[0], role)
		
		await ctx.send('Muted ✅ '+user.name+' 🔇')
	except discord.Forbidden:
		await ctx.send(embed=Forbidden)
		return
	except discord.HTTPException:
		await ctx.send('mute failed.')
		return
	except discord.ext.commands.errors.MissingPermissions:
		await ctx.send('User not found')
		return
	
#unmute command
@client.command(pass_context=True)
    
@commands.has_permissions(administrator=True)      

async def vocal(ctx,user:discord.Member):
	role = discord.utils.get(ctx.guild.roles,name='Muted')
	await ctx.message.delete()
	try:
		await discord.Member.remove_roles(ctx.message.mentions[0], role)
		await ctx.send(' ✅ '+user.name+' 🔉 is now Vocal')
	except discord.Forbidden:
		await ctx.send(embed=Forbidden)
		return
	except discord.HTTPException:
		await ctx.send('Failed to make Vocal.')
		return        	

#ping command
@client.command(pass_context = True)
async def ping(ctx):
    t1 = time.perf_counter()
    await ctx.trigger_typing()
    t2 = time.perf_counter()
    await ctx.send("Ping: {}ms".format(round((t2-t1)*1000)))
    return
 

#join command
@client.command(pass_context=True)
async def join(ctx):
	
	#author=ctx.message.author
	vc=ctx.author.voice.channel
	
	try:
		msg= await ctx.send('✅connecting to voice channel')
		await vc.connect(timeout=6.0)
		await asyncio.sleep(2)
		await msg.delete()
		await vc.connect(timeout=6.0)
		return 
	except discord.HTTPException:
		await ctx.send("already connected")
		return
	except discord.InvalidArgument:
		await ctx.send("please join a channel")
		return
		
	
#leave command		
@client.command()
async def leave(ctx):
#	voice_client(client.user)
	await ctx.voice_client.disconnect()
	msg= await ctx.send('✅dissconnected from voice channel')
	await asyncio.sleep(4)
	await msg.delete()
a=0

#ban command	  	  	  
@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)      
async def ban(ctx,user:discord.Member, *,reason=None):
	
    if a==0:
         await ctx.message.delete()  
        
    try:
        await user.ban()
        await ctx.send(user.name+' was banned ✅  Good bye '+user.name+'!')
	 
    except discord.Forbidden:
        await ctx.send(embed=Forbidden)
        return
    except discord.HTTPException:
        await ctx.send('ban failed.')
        return
        
#unban command
@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)
async def unban(ctx, *,member):
    ban_list = await ctx.guild.bans()

   
    member_name,member_discriminator=member.split('#')
    for ban_entry in ban_list:
    	user=ban_entry.user
    	if(member_name,member_discriminator)==(member_name,member_discriminator):
    		await ctx.guild.unban(user)
    		await ctx.send(f'Unbanned{user.mention}')
    		return

#getbans command
@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)		 		      	 		 		
async def bans(ctx):
    ban_list = await ctx.guild.bans()
    await ctx.send("Ban list:\n{}".format("\n".join([str(user) for user in ban_list])))

    # Show banned users
 #   await ctx.send("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

    
    if not ban_list:
    	
        await ctx.send('Ban list is empty.')
        return 	   
	
#Shut down command
@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)
async def shutdown(ctx):
	msg="Shut Down Success. \nBye :hugging:"
	msg_embed=discord.Embed(title="Shutting down...", description=msg,color=0x00ff00)
	await ctx.send(embed=msg_embed)
	await client.close()
	return

	
#invite command
@client.command(pass_context=True)
async def invite(ctx):
	await ctx.send(embed=inv_embed)
	return
client.run(os.getenv('Token'))
