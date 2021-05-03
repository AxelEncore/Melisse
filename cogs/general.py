import discord
from discord.ext import commands
from config import config
from discord import Embed, Status, Member, Color, Invite
from discord.utils import get
import os
import requests
import asyncio

from datetime import datetime
from os import environ
from sqlite3 import connect

class General(commands.Cog):
	""" owner commands
	"""

	def __init__(self, bot):
	    self.bot = bot

	@commands.command(aliases = ['ver', 'versions', 'версия', 'info', 'information', 'inform', 'bot', 'бот', 'мукышщт', 'штащкьфешщт', 'штащ'])
	async def version(self, ctx, amount = 1):
		await ctx.channel.purge(limit=amount)
		embed = discord.Embed(title = f"Меня зовут {config.BOT_NAME}",url = f'{config.BOT_URL}', color=0x2CB8F9)
		embed.add_field(name = f'Моя нынешняя версия: {config.VERSION}', value='▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁', inline=False)
		embed.add_field(name = f'Мой Создатель: @{config.AUTHOR}', value='▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁', inline=False)
		embed.add_field(name = f'Я создана для семьи: {config.FAMILY}', value=f'{config.FAMILY} сервер {config.DECRIPTION}', inline=False)
		embed.set_thumbnail(url = f'{config.BOT_IMG}')
		await ctx.send(embed=embed)



	#@commands.command(aliases = ['prof', 'зкщашду', 'prifil', 'user', 'профиль', 'пользователь', 'bio', 'био'])
	#async def profile(self, ctx):

	
def setup(bot):
    bot.add_cog(General(bot))
