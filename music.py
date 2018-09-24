import discord
import asyncio
import youtube_dl
import os
from discord.ext import commands
from discord.ext.commands import Bot


@bot.command(pass_context=True)
async def join(ctx):
    author=ctx.message.author
    vc=author.voice_channel
    await bot.join_voice_channel(vc)
    return

@bot.command(pass_context=True)
async def leave(ctx):
    server=ctx.message.server
    voice_client=bot.voice_client_in(server)
    await voice_client.disconnect()
    return
