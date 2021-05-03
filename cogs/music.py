import discord
from discord.ext import commands
from config import config
from discord import member, Embed
from discord.utils import get
import os
import asyncio

class Music(commands.Cog):
	""" owner commands
	"""

	def __init__(self, bot):
	    self.bot = bot


	@commands.command(pass_context=True)
	async def connect(self, ctx):
		await ctx.channel.purge(limit=1)
		channel = ctx.message.author.voice.channel
		await channel.connect()
		botMessage = await ctx.send(f":ballot_box_with_check: Подключилась")
		await asyncio.sleep(3)
		await botMessage.delete()

	@commands.command(pass_context=True)
	async def leave(self, ctx):
		await ctx.channel.purge(limit=1)
		server = ctx.message.guild.voice_client
		await server.disconnect()
		botMessage = await ctx.send(f":ballot_box_with_check: Отключилась")
		await asyncio.sleep(3)
		await botMessage.delete()



def setup(bot):
    bot.add_cog(Music(bot))
