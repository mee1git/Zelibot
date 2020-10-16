import os
import discord
import discord.utils
import time
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from random import randint

prefix = '!'

zeli_bot = Bot(command_prefix=prefix)

Bot.remove_command(zeli_bot, 'help')

post_id = 765207549187325963;

@zeli_bot.event
async def on_ready():
    print('Ок')

    await zeli_bot.change_presence(status=discord.Status.online, activity=discord.Game(" ЧСВшную сучку"))
@zeli_bot.event
async def on_command_error(ctx, error):
    pass

@Bot.command(zeli_bot)
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f"{author.mention} да-да, Хеллоу, блять... Нахуй иди!")

@Bot.command(zeli_bot)
@commands.has_permissions(administrator=True)
async def set_Lupa(ctx, member: discord.Member):
    zelibobka_role = discord.utils.get(ctx.message.guild.roles, name='Zelibobka')
    lupa_role = discord.utils.get(ctx.message.guild.roles, name='Лупа')
    await member.remove_roles(zelibobka_role)
    await member.add_roles(lupa_role)
    await ctx.send(f"{member.mention} стал Лупой :C")

@Bot.command(zeli_bot)
@commands.has_permissions(administrator=True)
async def set_zelibobka(ctx, member: discord.Member):
    zelibobka_role = discord.utils.get(ctx.message.guild.roles, name='Zelibobka')
    lupa_role = discord.utils.get(ctx.message.guild.roles, name='Лупа')
    await member.remove_roles(lupa_role)
    await member.add_roles(zelibobka_role)
    await ctx.send(f"{member.mention} стал зелибобкой :)")

@Bot.command(zeli_bot)
@commands.has_role(764468531206422538)
async def set_lupa(ctx, member: discord.Member):
    lupa_role = discord.utils.get(ctx.message.guild.roles, name='Лупа')
    await member.add_roles(lupa_role)
    await ctx.send(f"{member.mention}, {ctx.author.mention} сделал вас Лупой :Э")

@Bot.command(zeli_bot)
@commands.has_role(764467400300429312)
async def del_lupa(ctx, member: discord.Member):
    lupa_role = discord.utils.get(ctx.message.guild.roles, name='Лупа')
    await member.remove_roles(lupa_role)
    await ctx.send(f"{member.mention}, {ctx.author.mention} забрал у вас роль Лупы :C")

@Bot.command(zeli_bot)
@commands.has_permissions(administrator=True)
async def set_bot_inviter(ctx, member: discord.Member):
    bot_inviter_role = discord.utils.get(ctx.message.guild.roles, name='bot_inviter')
    await member.add_roles(bot_inviter_role)
    await ctx.send(f"{member.mention} стал бот_инвайтером, Аеееее, САСНЫЙ!!!")

@Bot.command(zeli_bot)
@commands.has_permissions(administrator=True)
async def del_bot_inviter(ctx, member: discord.Member):
    bot_inviter_role = discord.utils.get(ctx.message.guild.roles, name='bot_inviter')
    await member.remove_roles(bot_inviter_role)
    await ctx.send(f"{member.mention} перестал быть бот_инвайтером :ССССССССС")

@Bot.command(zeli_bot)
@commands.has_role(764864128383975437)
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(zeli_bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send(f'Зелибот присоединился к каналу: {channel}')

@Bot.command(zeli_bot)
@commands.has_role(764864128383975437)
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(zeli_bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await ctx.send(f'Зелибот решил уйти из канала: {channel}')
        await voice.disconnect()
    else:
        voice = await channel.disconnect()

@Bot.command(zeli_bot)
async def RR(ctx):
    await ctx.send(f'{ctx.author.mention} Крутим барабан...')
    time.sleep(5)
    a = randint(1, 6)
    if a == 1:
        await ctx.send(f'{ctx.author.mention} иди нахуй')
    else:
        await ctx.send(f'{ctx.author.mention}, ну ничего, как-нибудь, в другой раз сходишь нахуй...')


@Bot.command(zeli_bot)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount+1)

@Bot.command(zeli_bot)
async def help(ctx):
    emb = discord.Embed(title='Список команд Зелибота(Non-admin):', colour=0x2fff00, )
    emb.add_field(name=f'{prefix}help', value='Выводит список команд Зелибота в личные сообщения.', inline=False)
    emb.add_field(name=f'{prefix}hello', value='Зелибот поприветствует вас.', inline=False)
    emb.add_field(name=f'{prefix}clear [Кол-во сообщений]', value='Зелибот удалит 100 сообщений/[Кол-во сообщений]', inline=False)
    emb.add_field(name=f'{prefix}join', value='Пригласить Зелибота в голосовой чат. (Нужно: быть в голосовом чате; иметь роль bot_inviter)', inline=False)
    emb.add_field(name=f'{prefix}leave', value='Выгнать Зелибота из голосового чата. (Нужно: быть в голосовом чате; иметь роль bot_inviter)', inline=False)
    emb.add_field(name=f'{prefix}set_lupa [@Пользователь]',
                  value='Вы сделаете [@Пользователя] лупой. (Нужно иметь роль Лупа)', inline=False)
    emb.add_field(name=f'{prefix}del_lupa [@Пользователь]', value='вы заберёте роль Лупа у [@Пользователя]. (Нужно иметь роль Zelibobka)',
                  inline=False)
    emb.add_field(name=f'{prefix}RR', value='Русская рулетка, шанс 1 к 6 пойти нахуй', inline=False)
    emb1 = discord.Embed(title='Список команд Зелибота(admin):', colour=0x2fff00)
    emb1.add_field(name=f'{prefix}help_in', value='Выводит список команд Зелибота в данный чат', inline=False)
    emb1.add_field(name=f'{prefix}set_Lupa [@Пользователь]', value='[@Пользователь] станет лупой.', inline=False)
    emb1.add_field(name=f'{prefix}set_zelibobka [@Пользователь]', value='[@Пользователь] станет зелибобкой', inline=False)
    emb1.add_field(name=f'{prefix}set_bot_inviter [@Пользователь]', value='[@Пользователь] станет бот_инвайтером',
                   inline=False)
    emb1.add_field(name=f'{prefix}del_bot_inviter [@Пользователь]', value='[@Пользователь] перестанет быть бот_инвайтером',
                   inline=False)
    await ctx.message.author.send(embed=emb)
    await ctx.message.author.send(embed=emb1)
@Bot.command(zeli_bot)
@commands.has_permissions(administrator=True)
async def help_in(ctx):
    emb = discord.Embed(title='Список команд Зелибота(Non-admin):', colour=0x2fff00, )
    emb.add_field(name=f'{prefix}help', value='Выводит список команд Зелибота в личные сообщения', inline=False)
    emb.add_field(name=f'{prefix}hello', value='Зелибот поприветствует вас.', inline=False)
    emb.add_field(name=f'{prefix}clear [Кол-во сообщений]', value='Зелибот удалит 100 сообщений/[Кол-во сообщений]', inline=False)
    emb.add_field(name=f'{prefix}join', value='Пригласить Зелибота в голосовой чат. (Нужно: быть в голосовом чате; иметь роль bot_inviter)', inline=False)
    emb.add_field(name=f'{prefix}leave', value='Выгнать Зелибота из голосового чата. (Нужно: быть в голосовом чате; иметь роль bot_inviter)', inline=False)
    emb.add_field(name=f'{prefix}set_lupa [@Пользователь]', value='Вы сделаете [@Пользователя] лупой. (Нужно иметь роль Лупа)', inline=False)
    emb.add_field(name=f'{prefix}del_lupa [@Пользователь]', value='вы заберёте роль Лупа у [@Пользователя]. (Нужно иметь роль Zelibobka)', inline=False)
    emb.add_field(name=f'{prefix}RR', value='Русская рулетка, шанс 1 к 6 пойти нахуй', inline=False)
    emb1 = discord.Embed(title='Список команд Зелибота(admin):', colour=0x2fff00)
    emb1.add_field(name=f'{prefix}help_in', value='Выводит список команд Зелибота в данный чат', inline=False)
    emb1.add_field(name=f'{prefix}set_Lupa [@Пользователь]', value='[@Пользователь] станет лупой.', inline=False)
    emb1.add_field(name=f'{prefix}set_zelibobka [@Пользователь]', value='[@Пользователь] станет зелибобкой', inline=False)
    emb1.add_field(name=f'{prefix}set_bot_inviter [@Пользователь]', value='[@Пользователь] станет бот_инвайтером',
                   inline=False)
    emb1.add_field(name=f'{prefix}del_bot_inviter [@Пользователь]', value='[@Пользователь] перестанет быть бот_инвайтером',
                   inline=False)
    await ctx.send(embed=emb)
    await ctx.send(embed=emb1)

@join.error
async def join_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send(f'{ctx.author.mention}, Зелибот не общается с кем попало, для этой команды нужна роль - bot_inviter')

@leave.error
async def leave_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send(f'{ctx.author.mention}, хотел выгнать Зелибота? А может тебя выгнать? Для этой команды нужна роль - bot_inviter')

@set_lupa.error
async def set_lupa_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send(f'{ctx.author.mention}, Нужно быть лупой, чтобы сделать кого-нибудь лупой...')

@del_lupa.error
async def del_lupa_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send(f'{ctx.author.mention}, Нужно быть зелибобкой, чтобы отобрать роль лупы...')


zeli_bot.run(os.environ['TOKEN'])