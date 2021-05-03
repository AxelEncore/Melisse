from typing import NamedTuple
import discord
from discord.ext import commands
from discord.ext.commands.core import guild_only
from config import config
from discord import member, Embed
from discord.utils import get
import youtube_dl
import os
from discord.ext.commands import when_mentioned_or
import json
import asyncio

bot = commands.Bot(command_prefix = ">", pm_help=True, intents = discord.Intents.all())
bot.remove_command( 'help' )

@bot.event
async def on_member_join(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Подписчик☄️")
    await ctx.add_roles(role)

@bot.command()
async def ping(ctx):
	await ctx.message.delete()
	embed = Embed(title = f'Мой пинг: {bot.latency}!', color=0x08E8B2)
	botMessage = await ctx.send(embed=embed)
	await asyncio.sleep(5)
	await botMessage.delete()


@bot.command()
async def load(ctx, extension):
	if ctx.author.id == 273441439852003328:
		bot.load_extension(f"cogs.{extension}")
		await ctx.send("Loaded..")
	else:
		await ctx.send("Perm error")

@bot.command()
async def unload(ctx, extension):
	if ctx.author.id == 273441439852003328:
		bot.unload_extension(f"cogs.{extension}")
		await ctx.send("Loaded..")
	else:
		await ctx.send("Perm error")

@bot.command()
async def reload(ctx, extension):
	if ctx.author.id == 273441439852003328:
		bot.unload_extension(f"cogs.{extension}")
		bot.load_extension(f"cogs.{extension}")
		await ctx.send("Loaded..")
	else:
		await ctx.send("Perm error")

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_ready():

	print('запуск бота:', config.BOT_NAME, '...')

	await bot.change_presence(activity=discord.Streaming(name=f"твои мечты", url='https://www.twitch.tv/monstercat'))

	print(config.COMPLETE_SETUP_MESSAGE)

	print('Версия:', config.VERSION)

@bot.event
async def on_command_error(ctx,error):
	if isinstance(error, commands.CommandNotFound):
		embed = Embed(color = 0xFF3030)
		embed.add_field(name=f":x: ОЙ Ошибка", value="Я не знаю такой команды")
		botMessage = await ctx.send(embed=embed)
		await asyncio.sleep(3)
		await botMessage.delete()
	pass


@bot.command()
async def help (ctx):
	embed = discord.Embed(title = ":scroll:   Навигация по командам", description ="Description of commands in English on the bot page \n https://top.gg/bot/680718566986743837", color=0xe543ff)
	embed.add_field(name = '{}ping'.format(config.PREFIX), value='Проверка работоспособности и отображение пинга', inline=False)
	embed.add_field(name = '{}version'.format(config.PREFIX), value='Узнать версию бота', inline=False)
	embed.add_field(name = '{}clear'.format(config.PREFIX), value='`!clear [x]` - Очистка чата', inline=False)
	embed.add_field(name = '{}kick'.format(config.PREFIX), value='`!kick [участник] [причина]` - Кик пользователя', inline=False)
	embed.add_field(name = '{}ban'.format(config.PREFIX), value='`!ban [участник] [причина]` - Бан пользователя', inline=False)
	embed.add_field(name = '{}unban'.format(config.PREFIX), value='`!unban [участник]` - Разблокировать пользователя', inline=False)
	embed.add_field(name = '{}connect'.format(config.PREFIX), value='Подключаюсь к голосовому каналу', inline=False)
	embed.add_field(name = '{}leave'.format(config.PREFIX), value='Отключаюсь от голосового канала', inline=False)
	# embed.add_field(name = '{}play'.format(config.PREFIX), value='`!play [yt url]` - Проигрываю песню', inline=False)
	# embed.add_field(name = '{}pause'.format(config.PREFIX), value='Ставлю песню на паузу', inline=False)
	# embed.add_field(name = '{}resume'.format(config.PREFIX), value='Продолжаю воспроизведение', inline=False)
	# embed.add_field(name = '{}stop'.format(config.PREFIX), value='Останавливаю воспроизведение', inline=False)

	await ctx.channel.send(embed=embed)

	
#@bot.event
#async def on_message( message ):
#	await bot.process_commands( message )
#	embed = Embed(title="Осторожнее ты используешь запрещенные слова", color=0xF1602E)
#	msg = message.content.lower()
#	if msg in config.BAD_WORDS:
#		await message.delete()
#		await message.channel.send(embed=embed)


bot.run(config.TOKEN, bot=True, reconnect=True)
