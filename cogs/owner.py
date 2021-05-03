import discord
from discord.ext import commands
from config import config
from discord import member, Embed
from discord.utils import get
import os
import asyncio


class Owner(commands.Cog):
	""" owner commands
	"""

	def __init__(self, bot):
		self.bot = bot


	#@bot.command()
	#@commands.has_permissions(administrator = True)
	#@commands.has_permissions(manage_messages=True)
	#async def user_mute(ctx, member: discord.Member, *, reason= None):
	#	await ctx.channel.purge(limit=1)
	#	embed = Embed(color=0xff6614)
	#	embed.add_field(name='Кем', value=f"```{ctx.author.display_name}```", inline=True)
	#	embed.add_field(name='Причина', value=f"```{reason}```", inline=True)
	#	embed.set_author(name=f'Пользователю {member} отключен чат', icon_url=member.avatar_url)
	#	await member.user_mute(reason=reason)
	#	await ctx.channel.send(embed=embed)
		#mute = discord.utils.get(ctx.message.guild.roles, name = 'mute')
	@commands.command(aliases = ['очисти', 'del', 'delete', 'очистить', 'сдуфк', 'вуд', 'вудуеу', 'CLEAR', 'DEL', 'СДУФК'])
	@commands.has_permissions(administrator = True)
	async def clear(self, ctx, amount: int):
		await ctx.channel.purge(limit=amount)
		embed = Embed(description = f":white_check_mark: удалила сообщений: {amount}", color = 0x5FDA14)
		botMessage = await ctx.send(embed=embed)
		await asyncio.sleep(3)
		await botMessage.delete()

	@commands.command(aliases = ['кик', 'кикнуть', 'лшсл', 'kikc', 'kik', 'kic', 'KICK', 'KIKC', 'KIK', 'KIC'])
	@commands.has_permissions( administrator = True)
	@commands.has_permissions( kick_members = True, manage_roles=True, ban_members=True)
	async def kick(self, ctx, member: discord.Member, *, reason=None):
		await ctx.channel.purge(limit=1)
		embed = discord.Embed(color=0xff6614)
		embed.add_field(name='Кем', value=f"```{ctx.author.display_name}```", inline=True)
		embed.add_field(name='Причина', value=f"```{reason}```", inline=True)
		embed.set_author(name=f'Пользователь {member} был кикнут', icon_url=member.avatar_url)
		await member.kick(reason=reason)
		await ctx.channel.send(embed=embed)

	@commands.command(aliases = ['бан', 'забанить', 'bb', 'bna', 'ифт', 'BAN', 'BNA', 'ИФТ'])
	@commands.has_permissions(administrator = True)
	@commands.has_permissions(ban_members = True)
	async def ban(self, ctx, member: discord.Member, *, reason= None):
		await ctx.channel.purge(limit=1)

		embed = Embed(color=0xff6614)
		embed.add_field(name='Кем', value=f"```{ctx.author.display_name}```", inline=True)
		embed.add_field(name='Причина', value=f"```{reason}```", inline=True)
		embed.set_author(name=f'Пользователь {member} был забанен', icon_url=member.avatar_url)
		await member.ban(reason=reason)
		await ctx.channel.send(embed=embed)

	@commands.command(aliases = ['разбан', 'разбанить', 'unbb', 'unbna', 'гтифт', 'UNBAN', 'UNBNA', 'ГТИФТ'])
	@commands.has_permissions(administrator = True)
	@commands.has_permissions(ban_members = True)
	async def unban(self, ctx, member: str, reason: str = None):
		await ctx.channel.purge(limit=1)

		banned_users = await ctx.guild.bans()
		#if not banned_users:
		#	embed = Embed(title="Ой! Что-то пошло не так:", description="В бане сейчас никого нет", color=0xe74c3c)
		#	await ctx.send(embed=embed); return
		for ban_entry in banned_users:
			user = ban_entry.user
			await ctx.guild.unban(user)
			embed = Embed(color=0x2ecc71)
			embed.add_field(name='Кем', value=f"```{ctx.author.display_name}```")
			embed.set_author(name=f'Пользователь {member} был разблокирован')
			await ctx.send(embed=embed); return
			#await ctx.send(f'```пользователь {member} разблокирован```')

	@commands.command(aliase = [])
	@commands.has_permissions(administrator=True)
	async def mute(self, ctx, member:discord.Member, duration, *, reason=None):
		unit = duration[-1]
		print(f'{unit}')
		if unit == 'с':
			time = int(duration[:-1])
			longunit = 'секунд'
		elif unit == 'м':
			time = int(duration[:-1]) * 60
			longunit = 'минут'
		elif unit == 'ч':
			time = int(duration[:-1]) * 60 * 60
			longunit = 'часов'
		else:
			await ctx.send('Неправильно! Пиши `c`, `м`, `ч`')
			return

		progress = await ctx.send('Пользователь теперь замучен!')
		try:
			for channel in ctx.guild.text_channels:
				await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(send_messages = False), reason=reason)

			for channel in ctx.guild.voice_channels:
				await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(speak=False), reason=reason)
		except:
			success = False
		else:
			success = True

		await ctx.send(f'{member} замучен на {duration}')
		await asyncio.sleep(time)
		try:
			for channel in ctx.guild.channels:
				 await channel.set_permissions(member, overwrite=None, reason=reason)
		except:
			pass

	#--------------------------------------/ERRORS/------------------------------------#

	@clear.error
	async def clear_error(self, ctx, error):
		if isinstance( error, commands.MissingRequiredArgument):
			await ctx.message.delete()
			embed = Embed(color = 0xFF3030)
			embed.add_field(name=f":x: ОЙ Ошибка", value="вы не ввели количество сообщений!")
			botMessage = await ctx.send(embed=embed)
			await asyncio.sleep(3)
			await botMessage.delete()
		if isinstance (error, commands.MissingPermissions):
			await ctx.message.delete()
			embed = Embed(color = 0xFF3030)
			embed.add_field(name=f":x: Ну-ну, ты пока не настолько крут", value="у тебя нет прав на это")
			botMessage = await ctx.send(embed=embed)
			await asyncio.sleep(3)
			await botMessage.delete()
	@kick.error
	async def kick_error(self, ctx, error):
		if isinstance( error, commands.MissingRequiredArgument):
			await ctx.message.delete()
			embed = Embed(color = 0xFF3030)
			embed.add_field(name=f":x: ОЙ Ошибка", value="вы не ввели значение!")
			botMessage = await ctx.send(embed=embed)
			await asyncio.sleep(3)
			await botMessage.delete()
		if isinstance (error, commands.MissingPermissions):
			await ctx.message.delete()
			embed = Embed(color = 0xFF3030)
			embed.add_field(name=f":x: Ну-ну, ты пока не настолько крут", value="у тебя нет прав на это")
			botMessage = await ctx.send(embed=embed)
			await asyncio.sleep(3)
			await botMessage.delete()

def setup(bot):
	bot.add_cog(Owner(bot))
