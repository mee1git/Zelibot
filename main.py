import os
import time
from random import randint

import discord
import discord.utils
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get

import requests
from PIL import Image, ImageFont, ImageDraw
import io


prefix = '!'

zeli_bot = Bot(command_prefix=prefix)

Bot.remove_command(zeli_bot, 'help')


@zeli_bot.event
async def on_ready():
    print('Ок')

    await zeli_bot.change_presence(status=discord.Status.online, activity=discord.Game(" ЧСВшную сучку"))
@zeli_bot.event
async def on_command_error(ctx, error):
    pass

@Bot.command(zeli_bot, aliases=['привет'])
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f"{author.mention} да-да, Хеллоу, блять... Нахуй иди!")

@Bot.command(zeli_bot, aliases=['сделать_Лупой'])
@commands.has_permissions(administrator=True)
async def set_Lupa(ctx, member: discord.Member):
    zelibobka_role = discord.utils.get(ctx.message.guild.roles, name='Zelibobka')
    lupa_role = discord.utils.get(ctx.message.guild.roles, name='Лупа')
    await member.remove_roles(zelibobka_role)
    await member.add_roles(lupa_role)
    await ctx.send(f"{member.mention} стал Лупой :C")

@Bot.command(zeli_bot, aliases=['сделать_зелибобкой'])
@commands.has_permissions(administrator=True)
async def set_zelibobka(ctx, member: discord.Member):
    zelibobka_role = discord.utils.get(ctx.message.guild.roles, name='Zelibobka')
    lupa_role = discord.utils.get(ctx.message.guild.roles, name='Лупа')
    await member.remove_roles(lupa_role)
    await member.add_roles(zelibobka_role)
    await ctx.send(f"{member.mention} стал зелибобкой :)")

@Bot.command(zeli_bot, aliases=['сделать_лупой'])
@commands.has_role(764468531206422538)
async def set_lupa(ctx, member: discord.Member):
    lupa_role = discord.utils.get(ctx.message.guild.roles, name='Лупа')
    await member.add_roles(lupa_role)
    await ctx.send(f"{member.mention}, {ctx.author.mention} сделал вас Лупой :Э")

@Bot.command(zeli_bot, aliases=['больше_не_лупа'])
@commands.has_role(764467400300429312)
async def del_lupa(ctx, member: discord.Member):
    lupa_role = discord.utils.get(ctx.message.guild.roles, name='Лупа')
    await member.remove_roles(lupa_role)
    await ctx.send(f"{member.mention}, {ctx.author.mention} забрал у вас роль Лупы :C")

@Bot.command(zeli_bot, aliases=['сделать_бот_инвайтером'])
@commands.has_permissions(administrator=True)
async def set_bot_inviter(ctx, member: discord.Member):
    bot_inviter_role = discord.utils.get(ctx.message.guild.roles, name='bot_inviter')
    await member.add_roles(bot_inviter_role)
    await ctx.send(f"{member.mention} стал бот_инвайтером, Аеееее, САСНЫЙ!!!")

@Bot.command(zeli_bot, aliases=['больше_не_бот_инвайтер'])
@commands.has_permissions(administrator=True)
async def del_bot_inviter(ctx, member: discord.Member):
    bot_inviter_role = discord.utils.get(ctx.message.guild.roles, name='bot_inviter')
    await member.remove_roles(bot_inviter_role)
    await ctx.send(f"{member.mention} перестал быть бот_инвайтером :ССССССССС")

@Bot.command(zeli_bot, aliases=['подключить'])
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

@Bot.command(zeli_bot, aliases=['кикнуть'])
@commands.has_role(764864128383975437)
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(zeli_bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await ctx.send(f'Зелибот решил уйти из канала: {channel}')
        await voice.disconnect()
    else:
        voice = await channel.disconnect()

@Bot.command(zeli_bot, aliases=['русская_рулетка'])
async def RR(ctx):
    await ctx.send(f'{ctx.author.mention} Крутим барабан...')
    time.sleep(5)
    a = randint(1, 6)
    if a == 1:
        await ctx.send(f'{ctx.author.mention} иди нахуй')
    else:
        await ctx.send(f'{ctx.author.mention}, ну ничего, как-нибудь, в другой раз сходишь нахуй...')


@Bot.command(zeli_bot, aliases=['отчистить'])
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount+1)

@Bot.command(zeli_bot, aliases=['карта'])
async def get_card(ctx):
    img = Image.new('RGBA', (400, 200), '#012136')
    url = str(ctx.author.avatar_url)[:-10]

    resp = requests.get(url, stream=True)
    resp = Image.open(io.BytesIO(resp.content))
    resp = resp.convert('RGBA')
    resp = resp.resize((100, 100), Image.ANTIALIAS)

    img.paste(resp, (15, 15, 115, 115))

    idraw = ImageDraw.Draw(img)
    name = ctx.author.name
    mention = ctx.message.author.display_name
    tag = ctx.author.discriminator
    role = ctx.author.top_role.name

    if role == 'Zeliboba':
        col = '#46bf36'
    elif role == 'Zelibobka':
        col = '#78ff66'
    elif role == 'Лупа':
        col = '#d466ff'
    elif role == 'Пупа':
        col = '#ff6666'
    else:
        col = '#7cfce7'

    headline = ImageFont.truetype('fonts/3.otf', size=20)
    undertext = ImageFont.truetype('fonts/2.ttf', size=15)
    idraw.text((145, 15), 'Карта участника сервера', font=headline, fill=col)
    idraw.text((145, 50), f'id: {ctx.author.id}', font=undertext, fill=col)
    idraw.text((145, 70), f'Никнейм в discord: {name}#{tag}', font=undertext, fill=col)
    idraw.text((145, 90), f'Никнейм на сервере: {mention}', font=undertext, fill=col)
    idraw.text((145, 110), f'Роль: {role}', font=undertext, fill=col)
    idraw.text((15, 180), f'Сервер: {ctx.message.guild.name}', font=undertext, fill=col)

    img.save('cards/user_card.png')

    await ctx.send(file=discord.File(fp='cards/user_card.png'))



@Bot.command(zeli_bot, aliases=['ПАМАГИТЕ'])
async def help(ctx):
    emb = discord.Embed(title='Список команд Зелибота(Non-admin):', colour=0x2fff00, )
    emb.add_field(name=f'{prefix}help(ПАМАГИТЕ)', value='Выводит список команд Зелибота в личные сообщения.', inline=False)
    emb.add_field(name=f'{prefix}hello(привет)', value='Зелибот поприветствует вас.', inline=False)
    emb.add_field(name=f'{prefix}clear(отчистить) [Кол-во сообщений]', value='Зелибот удалит 100 сообщений/[Кол-во сообщений]', inline=False)
    emb.add_field(name=f'{prefix}join(подключить)', value='Пригласить Зелибота в голосовой чат. (Нужно: быть в голосовом чате; иметь роль bot_inviter)', inline=False)
    emb.add_field(name=f'{prefix}leave(кикнуть)', value='Выгнать Зелибота из голосового чата. (Нужно: быть в голосовом чате; иметь роль bot_inviter)', inline=False)
    emb.add_field(name=f'{prefix}set_lupa(сделать_лупой) [@Пользователь]',
                  value='Вы сделаете [@Пользователя] лупой. (Нужно иметь роль Лупа)', inline=False)
    emb.add_field(name=f'{prefix}del_lupa(больше_не_лупа) [@Пользователь]', value='вы заберёте роль Лупа у [@Пользователя]. (Нужно иметь роль Zelibobka)',
                  inline=False)
    emb.add_field(name=f'{prefix}RR(русская_рулетка)', value='Русская рулетка, шанс 1 к 6 пойти нахуй', inline=False)
    emb.add_field(name=f'{prefix}get_card(карта)', value='Выдаёт карту пользователя серевера, ей можно флексить где угодно.', inline=False)
    emb1 = discord.Embed(title='Список команд Зелибота(admin):', colour=0x2fff00)
    emb1.add_field(name=f'{prefix}help_in(ПАМАГИТЕ_здесь)', value='Выводит список команд Зелибота в данный чат', inline=False)
    emb1.add_field(name=f'{prefix}set_Lupa(сделать_Лупой) [@Пользователь]', value='[@Пользователь] станет лупой.', inline=False)
    emb1.add_field(name=f'{prefix}set_zelibobka(сделать_зелибобкой) [@Пользователь]', value='[@Пользователь] станет зелибобкой', inline=False)
    emb1.add_field(name=f'{prefix}set_bot_inviter(сделать_бот_инвайтером) [@Пользователь]', value='[@Пользователь] станет бот_инвайтером',
                   inline=False)
    emb1.add_field(name=f'{prefix}del_bot_inviter(больше_не_бот_инвайтер) [@Пользователь]', value='[@Пользователь] перестанет быть бот_инвайтером',
                   inline=False)
    await ctx.message.author.send(embed=emb)
    await ctx.message.author.send(embed=emb1)
@Bot.command(zeli_bot, aliases=['ПАМАГИТЕ_здесь'])
@commands.has_permissions(administrator=True)
async def help_in(ctx):
    emb = discord.Embed(title='Список команд Зелибота(Non-admin):', colour=0x2fff00, )
    emb.add_field(name=f'{prefix}help(ПАМАГИТЕ)', value='Выводит список команд Зелибота в личные сообщения.',
                  inline=False)
    emb.add_field(name=f'{prefix}hello(привет)', value='Зелибот поприветствует вас.', inline=False)
    emb.add_field(name=f'{prefix}clear(отчистить) [Кол-во сообщений]',
                  value='Зелибот удалит 100 сообщений/[Кол-во сообщений]', inline=False)
    emb.add_field(name=f'{prefix}join(подключить)',
                  value='Пригласить Зелибота в голосовой чат. (Нужно: быть в голосовом чате; иметь роль bot_inviter)',
                  inline=False)
    emb.add_field(name=f'{prefix}leave(кикнуть)',
                  value='Выгнать Зелибота из голосового чата. (Нужно: быть в голосовом чате; иметь роль bot_inviter)',
                  inline=False)
    emb.add_field(name=f'{prefix}set_lupa(сделать_лупой) [@Пользователь]',
                  value='Вы сделаете [@Пользователя] лупой. (Нужно иметь роль Лупа)', inline=False)
    emb.add_field(name=f'{prefix}del_lupa(больше_не_лупа) [@Пользователь]',
                  value='вы заберёте роль Лупа у [@Пользователя]. (Нужно иметь роль Zelibobka)',
                  inline=False)
    emb.add_field(name=f'{prefix}RR(русская_рулетка)', value='Русская рулетка, шанс 1 к 6 пойти нахуй', inline=False)
    emb.add_field(name=f'{prefix}get_card(карта)',
                  value='Выдаёт карту пользователя серевера, ей можно флексить где угодно.', inline=False)
    emb1 = discord.Embed(title='Список команд Зелибота(admin):', colour=0x2fff00)
    emb1.add_field(name=f'{prefix}help_in(ПАМАГИТЕ_здесь)', value='Выводит список команд Зелибота в данный чат',
                   inline=False)
    emb1.add_field(name=f'{prefix}set_Lupa(сделать_Лупой) [@Пользователь]', value='[@Пользователь] станет лупой.',
                   inline=False)
    emb1.add_field(name=f'{prefix}set_zelibobka(сделать_зелибобкой) [@Пользователь]',
                   value='[@Пользователь] станет зелибобкой', inline=False)
    emb1.add_field(name=f'{prefix}set_bot_inviter(сделать_бот_инвайтером) [@Пользователь]',
                   value='[@Пользователь] станет бот_инвайтером',
                   inline=False)
    emb1.add_field(name=f'{prefix}del_bot_inviter(больше_не_бот_инвайтер) [@Пользователь]',
                   value='[@Пользователь] перестанет быть бот_инвайтером',
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

# webhook added
