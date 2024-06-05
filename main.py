#telegram = @KAJOIQ
#discord = KAJOiq#0953
#Note: All rights reserved to - KAJO™

# تضمين مكتبة دسكورد
import discord
import os
from discord_buttons_plugin import *
from discord.ext import commands, tasks
import random
from random import choice
import string
from flask import redirect
import requests
import json
import googletrans
from datetime import datetime
from googletrans import Translator
from urllib.parse import quote_plus
import sqlite3
import pandas
# سيرفر لإبقاء البوت مفعل اون لاين
#from keep_alive import keep_alive


# علامة البرفكس الخاصة بالبوت
PREFIX_SYM = ['$', '!', '+', '#', '?', '.', ';']
bot = commands.Bot(command_prefix=PREFIX_SYM, intents=discord.Intents.all(), help_command=None)

## characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                     [2, 5, 8], [0, 4, 8], [2, 4, 6]]

# اضافة البوتن الى البوت
buttons = ButtonsClient(bot)

st = ['Porn Movements', '$help', 'With KAJO', 'Fuck Society']


###########################
# حدث البوت أثناء التنفيذ مباشرةً
@bot.event
async def on_ready():
    #db = sqlite3.connect('main.sqlite')
    #cursor = db.cursor()
    #cursor.execute('''
    #CREATE TABLE IF NOT EXISTS main(
    #gulid_name TEXT,
    #gulid_id TEXT,
    #channel_id TEXT,
    #message_id TEXT
    #)
    #''')
    change_status.start()
    print(f"We've logged in as {bot.user}.")

    # status (playing)
    #await bot.change_presence(status=discord.Status.idle, activity=discord.Game("$help"))

    # status (watching)
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Pornhub"))

    # status (streaming)
    #await bot.change_presence(activity=discord.Streaming(name="My Stream", url=""))


@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(status=discord.Status.idle,
                              activity=discord.Game(choice(st)))


###########################

###########################
#@bot.event
#async def on_message_delete(message):
    #idchannel= (f"{message.channel.id}")
    #channel=bot.get_channel(idchannel)
    #user = message.author
    #channel=message.channel
    #await channel.send(f"```User:``` {user.mention} \n ```Deleted Message:``` {message.content} \n ```In Channel:``` {channel.mention}")
###########################


@bot.event
async def on_message(message):
    user = message.author
    channel = message.channel

    ###########################
     #Database
    db = sqlite3.connect('main.sqlite')
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS main(
    gulid_name TEXT,
    gulid_id TEXT,
    channel_id TEXT,
    message_id TEXT
    )
    ''') 
    db = sqlite3.connect('main.sqlite')
    cursor = db.cursor()
    cursor.execute(f"SELECT channel_id FROM main WHERE gulid_id = {user.id}")
    row = cursor.fetchone()
    if row is None:
        sql = (f"INSERT INTO main (gulid_name, gulid_id, channel_id, message_id) VALUES (?, ?, ?, ?)")
        val = (user.display_name, user.id, channel.id, message.id)
    elif row is not None:
        sql = (f"UPDATE main SET channel_id = ? WHERE gulid_name = ? AND gulid_id = ? AND message_id = ?")
        val = (channel.id, user.display_name, user.id, message.id)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()
    
    #End Database 
    ###########################

###########################
# Errors in command.
@bot.event
async def on_command_error(ctx, error):
    print(error)
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title='Error',
                              description="Command Not Available",
                              color=discord.Color.red(),
                              timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                         icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url='https://i.imgur.com/LxxYrFj.png')
        embed.add_field(name="Available commands",
                        value="**$**help",
                        inline=False)
        await ctx.reply(embed=embed)

# End errors in command.
###########################


###########################
# Help command.
@bot.command()
# help bot.
async def help(ctx, *, args=None):
    if args == "translate":
        embed = discord.Embed(color=discord.Color.blue(),
                                timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                            icon_url=ctx.author.avatar_url)
        embed.add_field(name="Message", value="Check your `DM`!", inline=False)
        await ctx.reply(embed=embed)
        await ctx.author.send("**Usage:** `$translate [language] [text]`\n**Example:** `$translate ar Hello World`\n\n**Language available:**\nAfrikaans=af\nAmharic=am\nArabic=ar\nAzerbaijani=az\nBelarusian=be\nBulgarian=bg\nBengali=bn\nBosnian=bs\nCatalan;Valencian=ca\nCorsican=co\nCzech=cs\nWelsh=cy\nDanish=da\nGerman=de\nEwe=ee\nGreek,Modern=el\nEnglish=en\nEsperanto=eo\nSpanish;Castilian=es\nEstonian=et\nBasque=eu\nPersian=fa\nFinnish=fi\nFrench=fr\nWesternFrisian=fy\nIrish=ga\nGaelic;ScottishGaelic=gd\nGalician=gl\nManx=gv\nHebrew=he\nHindi=hi\nCroatian=hr\nHaitian;HaitianCreole=ht\nHungarian=hu\nArmenian=hy\nIgbo=ig\nIndonesian=id\nIcelandic=is\nItalian=it\nJapanese=ja\nKazakh=kk\nGeorgian=ka\nCentralKhmer=km\nKannada=kn\nKorean=ko\nKurdish=ku\nKyrgyz=ky\nLatin=la\nLuxembourgish;Letzeburgesch=lb\nLithuanian=lt\nLatvian=lv\nMalagasy=mg\nMaori=mi\nMacedonian=mk\nMalay=ms\nMaltese=mt\nHmong;Mong=mn\nMarathi=mr\nMalayalam=ml\nBurmese=my\nNepali=ne\nDutch;Flemish=nl\nNorwegian=no\nOriya=or\nPapiamento=pa\nPolish=pl\nPortuguese=pt\nRomanian=ro\nRussian=ru\nSinhala;Sinhalese=si\nSlovak=sk\nSlovenian=sl\nNorthernSami=sm\nShona=sn\nSomali=so\nAlbanian=sq\nSerbian=sr\nSwedish=sv\nSwahili=sw\nTamil=ta\nTelugu=te\nTajik=tg\nThai=th\nTagalog=tl\nTurkish=tr\nUkrainian=uk\nUrdu=ur\nUzbek=uz\nVietnamese=vi\nWelsh=cy\nXhosa=xh\nYiddish=yi\nYoruba=yo\nZulu=zu\n")   
    #member = ctx.author
    #await member.send(""  "")
    elif args == "password":
        embed = discord.Embed(color=discord.Color.blue(),
                                timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                            icon_url=ctx.author.avatar_url)
        embed.add_field(name="Message", value="Check your `DM`!", inline=False)
        await ctx.reply(embed=embed)
        await ctx.author.send("**Usage:** `$password [Password limited]`\n**Example:**\n$password 10")
    elif args == "userinfo":
        embed = discord.Embed(color=discord.Color.blue(),
                                timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                            icon_url=ctx.author.avatar_url)
        embed.add_field(name="Message", value="Check your `DM`!", inline=False)
        await ctx.reply(embed=embed)
        await ctx.author.send("**Usage:** `$userinfo` or `$userinfo [user]`\n**Example:**\n$userinfo @user")
    elif args == "clear_chat":
        embed = discord.Embed(color=discord.Color.blue(),
                                timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                            icon_url=ctx.author.avatar_url)
        embed.add_field(name="Message", value="Check your `DM`!", inline=False)
        await ctx.reply(embed=embed)
        await ctx.author.send("**Usage:** `$clear_chat [Limited]`\n**Example:**\n$clear_chat 10")
    elif args == "memes":
        embed = discord.Embed(color=discord.Color.blue(),
                                timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                            icon_url=ctx.author.avatar_url)
        embed.add_field(name="Message", value="Check your `DM`!", inline=False)
        await ctx.reply(embed=embed)
        await ctx.author.send("**Usage:** `$memes`\n**Example:**\n$memes")
    elif args == "help":
        embed = discord.Embed(color=discord.Color.blue(),
                                timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                            icon_url=ctx.author.avatar_url)
        embed.add_field(name="Message", value="Check your `DM`!", inline=False)
        await ctx.reply(embed=embed)
        await ctx.author.send("**Usage:** `$help` or `$help [commands]`\n**Example:**\n$help or $help translate")
    elif args == "bitcoin":
        embed = discord.Embed(color=discord.Color.blue(),
                                timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                            icon_url=ctx.author.avatar_url)
        embed.add_field(name="Message", value="Check your `DM`!", inline=False)
        await ctx.reply(embed=embed)
        await ctx.author.send("**Usage:** `$bitcoin`\n**Example:**\n$bitcoin")
    elif args == "python":
        embed = discord.Embed(color=discord.Color.blue(),
                                timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                            icon_url=ctx.author.avatar_url)
        embed.add_field(name="Message", value="Check your `DM`!", inline=False)
        await ctx.reply(embed=embed)
        await ctx.author.send("**Usage:** `$python [Block_code] with (```python)`\n**Example:**\n$python ```python\nprint('Hello World')\n```")
    elif args == "cpp":
        embed = discord.Embed(color=discord.Color.blue(),
                                timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                            icon_url=ctx.author.avatar_url)
        embed.add_field(name="Message", value="Check your `DM`!", inline=False)
        await ctx.reply(embed=embed)
        await ctx.author.send("**Usage:** `$cpp [Block_code] with (```cpp)`\n**Example:**\n$cpp ```cpp\n#include <iostream>\nint main()\n{\n std::cout << \"Hello World\";\n    return 0;\n}\n```")
    elif args == "java":
        embed = discord.Embed(color=discord.Color.blue(),
                                timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                            icon_url=ctx.author.avatar_url)
        embed.add_field(name="Message", value="Check your `DM`!", inline=False)
        await ctx.reply(embed=embed)
        await ctx.author.send("**Usage:** `$java [Block_code] with (```java)`\n**Example:**\n$java ```java\npublic class Main\n{\n    public static void main(String[] args)\n    {\n        System.out.println(\"Hello World\");\n    }\n}\n```")
    elif args == "tictactoe":
        embed = discord.Embed(color=discord.Color.blue(),
                                timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                            icon_url=ctx.author.avatar_url)
        embed.add_field(name="Message", value="Check your `DM`!", inline=False)
        await ctx.reply(embed=embed)
        await ctx.author.send("**Usage:** `$tictactoe [@user1] [user2]`\n**Example:**\n$tictactoe @user1 @user2")
    else:
        embed = discord.Embed(title='Help',
                            description='$help `or` $help [commands]',
                            color=discord.Color.blue(),
                            timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=bot.user.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                        icon_url=ctx.author.avatar_url)
        embed.add_field(
            name='Original',
            value=
            "**$**help\n**$**password\n**$**userinfo\n**$**clear_chat\n**$**memes\n**$**translate\n",
            inline=False)
        embed.add_field(name='For Developer',
                        value="**$**bitcoin\n**$**python\n**$**cpp\n**$**java\n")
        embed.add_field(name='Games(x-o)',
                        value="**$**tictactoe\n**$**place\n",
                        inline=False)

        await ctx.reply(embed=embed)

        # برمجة البوتن الخاص بالبوت
        await buttons.send(
            #content="Hey there",
            channel=ctx.channel.id,
            components=[
                ActionRow([
                    Button(style=ButtonType().Link,
                        label="Contact Us",
                        url=f"https://t.me/Kajo10"),

                    #Button(
                    #style = ButtonType().Link,
                    #label = "Invite Bot",
                    #	url = f"https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot"
                    #),

                    #Button(
                    #style = ButtonType().Danger,
                    #label = "Don't click",
                    #custom_id = "danger",
                    #),

                    #Button(
                    #style = ButtonType().Secondary,
                    #label = "Hello",
                    #custom_id = "lol",
                    #)
                ])
            ])
        
        ###########################
        # Database 
        #db = sqlite3.connect('main.sqlite')
        #cursor = db.cursor()
        #cursor.execute(f"SELECT channel_id FROM main WHERE gulid_id = {ctx.author.id}")
        #row = cursor.fetchone()
        #if row is None:
            #sql = (f"INSERT INTO main (gulid_id, channel_id) VALUES (?, ?)")
            #val = (ctx.author.id, ctx.channel.id)
        #elif row is not None:
            #sql = (f"UPDATE main SET channel_id = ? WHERE gulid_id = ?")
            #val = (ctx.channel.id, ctx.author.id)
        #cursor.execute(sql, val)
        #db.commit()
        #cursor.close()
        #db.close()
        # End Database 
        ###########################
# End help command.
###########################


###########################
@bot.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:"
        ]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send(
            "```A game is already in progress! Finish it before starting a new one.```"
        )

@bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + "` wins!`")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("```It's a tie!```")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send(
                    "```Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.```"
                )
        else:
            await ctx.send("```It is not your turn.```")
    else:
        await ctx.send(
            "```Please start a new game using the $tictactoe command.```")

def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[
                condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True


# if error in command tictactoe (function).
@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title='Error',
            description="Please mention 2 players for this command.",
            color=discord.Color.red(),
            timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                         icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url='https://i.imgur.com/LxxYrFj.png')
        await ctx.reply(embed=embed)
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(
            title='Error',
            description=
            "Please make sure to mention/ping players (ie. <@688534433879556134>).",
            color=discord.Color.red(),
            timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                         icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url='https://i.imgur.com/LxxYrFj.png')
        await ctx.reply(embed=embed)


# End tictactoe error function command.


# if error in command place (function).
@place.error
async def place_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title='Error',
            description="Please enter a position you would like to mark.",
            color=discord.Color.red(),
            timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                         icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url='https://i.imgur.com/LxxYrFj.png')
        await ctx.reply(embed=embed)
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(
            title='Error',
            description="Please make sure to enter an integer.",
            color=discord.Color.red(),
            timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                         icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url='https://i.imgur.com/LxxYrFj.png')
        await ctx.reply(embed=embed)


# End place error function command.

# End tictactoe command.
###########################

###########################
# إضافة بوتن الى البوت
#@buttons.click
#async def cu(ctx):
# 	await ctx.reply(f"Hi {ctx.member.name}")

#@buttons.click
#async def invite(ctx):
# 	await ctx.reply(f"{ctx.member.name} has clicked the button.")

#@buttons.click
#async def danger(ctx):
#	  await ctx.reply(f"{ctx.member}, told'ya not to click!")

#@buttons.click
#async def lol(ctx):
# 	await ctx.reply("lol")
###########################


###########################
# Password command
@bot.command()
async def password(ctx, length: int):
    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    password_suggestion = "".join(password)
    #text_file = open('./database/DB.txt', 'a')
    #text_file.write('\n' + password_suggestion)
    #text_file.close()

    embed = discord.Embed(
        title='Password Generator',
        description=f"Generate a password of length {length}.",
        color=discord.Color.blue(),
        timestamp=ctx.message.created_at)
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed.set_footer(text=f"Requested by - {ctx.author}",
                     icon_url=ctx.author.avatar_url)
    embed.add_field(name="Result", value=f"{password_suggestion}")
    await ctx.reply(embed=embed)

@password.error
async def chat_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title='Error',
                              description="$password (Limited password)",
                              color=discord.Color.red(),
                              timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                         icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url='https://i.imgur.com/LxxYrFj.png')
        await ctx.reply(embed=embed)
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(
            title='Error',
            description="Please make sure to enter an integer.",
            color=discord.Color.red(),
            timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                         icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url='https://i.imgur.com/LxxYrFj.png')
        await ctx.reply(embed=embed)

# End password command
###########################


###########################
# Clear_chat command
@bot.command()
async def clear_chat(ctx, amount: int):
    await ctx.channel.purge(limit=amount)


@clear_chat.error
async def chat_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title='Error',
                              description="$clear_chat (Limited number)",
                              color=discord.Color.red(),
                              timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                         icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url='https://i.imgur.com/LxxYrFj.png')
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(
            title='Error',
            description="Please make sure to enter an integer.",
            color=discord.Color.red(),
            timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                         icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url='https://i.imgur.com/LxxYrFj.png')
        await ctx.reply(embed=embed)


# End clear_chat command
###########################

###########################
# Kick command.
#@bot.command()
#async def kick(ctx, member : discord.Member, *, reason=None):
#await member.kick(reason=reason)

# End kick command.
###########################


###########################
# Userinfo command
@bot.command()
async def userinfo(ctx, *, member: discord.Member = None):
    member = ctx.author if not member else member

    rolelist = []
    for role in member.roles:
        if role.name != "@everyone":
            rolelist.append(role.mention)
    showrole = ','.join(rolelist)

    embed = discord.Embed(color=discord.Color.blue(),
                          timestamp=ctx.message.created_at)

    embed.set_author(name=member._user, icon_url=member.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by - {ctx.author}",
                     icon_url=ctx.author.avatar_url)

    embed.add_field(name="ID", value=member.id, inline=False)
    embed.add_field(name="Guild name", value=member.display_name, inline=False)

    embed.add_field(
        name="Created at",
        value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
        inline=False)
    embed.add_field(
        name="Joined at",
        value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
        inline=False)

    embed.add_field(name=f"Roles ({len(rolelist)})",
                    value=" ".join([showrole]),
                    inline=False)
    embed.add_field(name=f"Top role",
                    value=member.top_role.mention,
                    inline=False)

    embed.add_field(name="Bot?", value=member.bot, inline=False)

    await ctx.reply(embed=embed)

# End userinfo command
###########################


###########################
# Translate command.
@bot.command()
async def translate(ctx, lang, *, tex):
    trans_text = Translator()
    translated = trans_text.translate(tex, dest=lang)
    embed = discord.Embed(title='Translate result',
                          description=f"```{translated.text}```",
                          color=discord.Color.blue(),
                          timestamp=ctx.message.created_at)
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed.set_footer(text=f"Requested by - {ctx.author}",
                     icon_url=ctx.author.avatar_url)

    await ctx.reply(embed=embed)

@translate.error
async def chat_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title='Error',
            description="$translate (any language) (Type to translate)",
            color=discord.Color.red(),
            timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                         icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url='https://i.imgur.com/LxxYrFj.png')

        await ctx.reply(embed=embed)

# End translate command.
###########################


##########################
# Bitcoin command.
@bot.command()
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value_price = response.json()['bpi']['USD']['rate']
    embed = discord.Embed(color=discord.Color.blue(),
                          timestamp=ctx.message.created_at)
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed.set_footer(text=f"Requested by - {ctx.author}",
                     icon_url=ctx.author.avatar_url)
    embed.add_field(
        name="Price of bitcoin",
        value=f"Bitcoin price is: ${value_price}",
    )
    await ctx.reply(embed=embed) 
                                                   
# End bitcoin command.
##########################


##########################
# memes command.
@bot.command()
async def memes(ctx):
    r = requests.get("https://meme-api.herokuapp.com/gimme")
    respon = r.json()
    nameauthor = respon['author']
    embed = discord.Embed(title=f'Posted by: {nameauthor}',
                          color=discord.Color.blue(),
                          timestamp=ctx.message.created_at)
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed.set_footer(text=f"Requested by - {ctx.author}",
                     icon_url=ctx.author.avatar_url)
    embed.set_image(url=respon['url'])
    embed.add_field(name="Post url", value=respon['postLink'])

    await ctx.reply(embed=embed)
   
# End memes command.
##########################





##########################
# Compiler part.
##########################
client_id = '807c999d348a36eae0c98ae90dd5ccda'
client_secret = '4e8bb2e3391657243541362115c5e56fe2562be8ca873ab8f565a8a001fd762'

def compilerPython(code):
    post_url = 'https://api.jdoodle.com/v1/execute'

    return json.loads(
        requests.post(post_url,
                      json={
                          "script": f"{code}",
                          "language": "python3",
                          "versionIndex": "3",
                          "clientId": f"{client_id}",
                          "clientSecret": f"{client_secret}"
                      }).content)

def compilerCpp(code):
    post_url = 'https://api.jdoodle.com/v1/execute'

    return json.loads(
        requests.post(post_url,
                      json={
                          "script": f"{code}",
                          "language": "cpp14",
                          "versionIndex": "3",
                          "clientId": f"{client_id}",
                          "clientSecret": f"{client_secret}"
                      }).content)

def compilerJava(code):
    post_url = 'https://api.jdoodle.com/v1/execute'

    return json.loads(
        requests.post(post_url,
                      json={
                          "script": f"{code}",
                          "language": "java",
                          "versionIndex": "1",
                          "clientId": f"{client_id}",
                          "clientSecret": f"{client_secret}"
                      }).content)

def compilerPhp(code):
    post_url = 'https://api.jdoodle.com/v1/execute'

    return json.loads(
        requests.post(post_url,
                      json={
                          "script": f"{code}",
                          "language": "php",
                          "versionIndex": "4",
                          "clientId": f"{client_id}",
                          "clientSecret": f"{client_secret}"
                      }).content)

def compilerRuby(code):
    post_url = 'https://api.jdoodle.com/v1/execute'

    return json.loads(
        requests.post(post_url,
                      json={
                          "script": f"{code}",
                          "language": "ruby",
                          "versionIndex": "4",
                          "clientId": f"{client_id}",
                          "clientSecret": f"{client_secret}"
                      }).content)

def compilerGo(code):
    post_url = 'https://api.jdoodle.com/v1/execute'

    return json.loads(
        requests.post(post_url,
                      json={
                          "script": f"{code}",
                          "language": "go",
                          "versionIndex": "4",
                          "clientId": f"{client_id}",
                          "clientSecret": f"{client_secret}"
                      }).content)

def compilerBash(code):
    post_url = 'https://api.jdoodle.com/v1/execute'

    return json.loads(
        requests.post(post_url,
                      json={
                          "script": f"{code}",
                          "language": "bash",
                          "versionIndex": "4",
                          "clientId": f"{client_id}",
                          "clientSecret": f"{client_secret}"
                      }).content)

def compilerRust(code):
    post_url = 'https://api.jdoodle.com/v1/execute'

    return json.loads(
        requests.post(post_url,
                      json={
                          "script": f"{code}",
                          "language": "rust",
                          "versionIndex": "4",
                          "clientId": f"{client_id}",
                          "clientSecret": f"{client_secret}"
                      }).content)

def compilerNodejs(code):
    post_url = 'https://api.jdoodle.com/v1/execute'

    return json.loads(
        requests.post(post_url,
                      json={
                          "script": f"{code}",
                          "language": "nodejs",
                          "versionIndex": "4",
                          "clientId": f"{client_id}",
                          "clientSecret": f"{client_secret}"
                      }).content)

def compilerSql(code):
    post_url = 'https://api.jdoodle.com/v1/execute'

    return json.loads(
        requests.post(post_url,
                      json={
                          "script": f"{code}",
                          "language": "sql",
                          "versionIndex": "4",
                          "clientId": f"{client_id}",
                          "clientSecret": f"{client_secret}"
                      }).content)

def compilerC(code):
    post_url = 'https://api.jdoodle.com/v1/execute'

    return json.loads(
        requests.post(post_url,
                      json={
                          "script": f"{code}",
                          "language": "c",
                          "versionIndex": "4",
                          "clientId": f"{client_id}",
                          "clientSecret": f"{client_secret}"
                      }).content)

##########################
@bot.command()
async def cpp(ctx, *, code: str):
    #co = list(code)
    #t1 = ''.join(co[6:-3])
    #text_file = open('./database/DB.txt', 'a')
    #text_file.write('\n\n' + code)
    #text_file.close()
    if '`' in code:
        try:
            if len(code) < 500:
                if not os.path.exists("code.cpp"):
                    with open("code.cpp", 'w') as f:
                        f.write(code[6:-3])
                else:
                    os.remove("code.cpp")
                    with open("code.cpp", 'w') as f:
                        f.write(code[6:-3])
   
                text_file = open("code.cpp", 'r')
                await ctx.reply(
                    f"**Output:**\n```yaml\n{compilerCpp(code=text_file.read())['output']}```"
                )
            else:
                code = code[6:-3]
                com = compilerCpp(code=code)['output']
                open("output.txt", "w").write(com)
                await ctx.send(file=discord.File("output.txt"))
        except:
            code = code[6:-3]
            com = compilerCpp(code=code)['output']
            open("output.txt", "w").write(com)
            await ctx.send(file=discord.File("output.txt"))

    else:
        embed = discord.Embed(
            title='Error',
            description=
            "Please, type your code in (code block) by using triple backticks (```cpp in the begin & end) and try again.",
            color=discord.Color.red(),
            timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                         icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url='https://i.imgur.com/LxxYrFj.png')
        await ctx.reply(embed=embed)

    #text_file = open("code.cpp", 'r')
    #await ctx.reply(f"**Output:**\n```yaml\n{compilerCpp(code=text_file.read())['output']}```")
 
@cpp.error
async def chat_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title='Error',
            description="$cpp (type your code in code_block)",
            color=discord.Color.red(),
            timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                         icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url='https://i.imgur.com/LxxYrFj.png')
        await ctx.reply(embed=embed)

##########################


##########################
@bot.command()
async def python(ctx, *, code):
    #text_file = open('./database/DB.txt', 'a')
    #text_file.write('\n\n' + code)
    #text_file.close()
    if '`' in code:
        try:
            if len(code) < 500:
                if not os.path.exists("code.py"):
                    with open("code.py", 'w') as f:
                        f.write(code[9:-3])
                else:
                    os.remove("code.py")
                    with open("code.py", 'w') as f:
                        f.write(code[9:-3])
   
                text_file = open("code.py", 'r')
                await ctx.reply(
                    f"**Output:**\n```yaml\n{compilerPython(code=text_file.read())['output']}```"
                )
            else:
                code = code[9:-3]
                com = compilerPython(code=code)['output']
                open("output.txt", "w").write(com)
                await ctx.send(file=discord.File("output.txt"))
        except:
            code = code[9:-3]
            com = compilerPython(code=code)['output']
            open("output.txt", "w").write(com)
            await ctx.send(file=discord.File("output.txt"))

    else:
        embed = discord.Embed(
            title='Error',
            description=
            "Please, type your code in (code block) by using triple backticks (```python in the begin & end) and try again.",
            color=discord.Color.red(),
            timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                         icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url='https://i.imgur.com/LxxYrFj.png')
        await ctx.reply(embed=embed)

    #text_file = open("code.py", 'r')
    #await ctx.reply(f"**Output:**\n```yaml\n{compilerPython(code=text_file.read())['output']}```")
    
@python.error
async def chat_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title='Error',
            description="$python (type your code in code_block)",
            color=discord.Color.red(),
            timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                         icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url='https://i.imgur.com/LxxYrFj.png')
        await ctx.reply(embed=embed)

##########################


##########################
@bot.command()
async def java(ctx, *, code):
    #text_file = open('./database/DB.txt', 'a')
    #text_file.write('\n\n' + code)
    #text_file.close()
    if '`' in code:
        try:
            if len(code) < 500:
                if not os.path.exists("code.java"):
                    with open("code.java", 'w') as f:
                        f.write(code[7:-3])
                else:
                    os.remove("code.java")
                    with open("code.java", 'w') as f:
                        f.write(code[7:-3])
   
                text_file = open("code.java", 'r')
                await ctx.reply(
                    f"**Output:**\n```yaml\n{compilerJava(code=text_file.read())['output']}```"
                )
            else:
                code = code[7:-3]
                com = compilerJava(code=code)['output']
                open("output.txt", "w").write(com)
                await ctx.send(file=discord.File("output.txt"))
        except:
            code = code[7:-3]
            com = compilerJava(code=code)['output']
            open("output.txt", "w").write(com)
            await ctx.send(file=discord.File("output.txt"))

    else:
        embed = discord.Embed(
            title='Error',
            description=
            "Please, type your code in (code block) by using triple backticks (```java in the begin & end) and try again.",
            color=discord.Color.red(),
            timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                         icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url='https://i.imgur.com/LxxYrFj.png')
        await ctx.reply(embed=embed)
    #text_file = open("code.java", 'r')
    #await ctx.reply(f"**Output:**\n```yaml\n{compilerJava(code=text_file.read())['output']}```")
   
@java.error
async def chat_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title='Error',
            description="$java (type your code in code_block)",
            color=discord.Color.red(),
            timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by - {ctx.author}",
                         icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url='https://i.imgur.com/LxxYrFj.png')
        await ctx.reply(embed=embed)

##########################
##########################
# End compiler part.
##########################


##########################

# ربط السيرفر وابقاء الكود مُفعّل
#keep_alive()

# عمل تنفيذ للبوت الخاص الذي يعمل من عن طريق الــتوكن الخاص به
TOKEN = '[BOT TOKEN]'

bot.run(TOKEN)
##########################