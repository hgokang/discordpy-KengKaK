

import json
import re
from typing import ContextManager
from datetime import datetime
import discord, asyncio
import random
import os
from discord import client
from discord import voice_client
from discord import activity
from discord.ext import commands
import sys
from pathlib import Path
from discord import Member
from typing import Optional
import googletrans
from discord.utils import get
from wavelink import player
from asyncio import sleep as s








bot = commands.Bot(command_prefix='+',help_command=None,case_intensitive=True , owner_id=548777470829133824)










def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
                

@bot.command(brief="สั่งรีบอท", help="พิม+restart เพื่อรีบอท")
async def restart(ctx):
    await ctx.send("กำลังเริ่มต้นใหม่ ใน5วินาที")
    restart_program()


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="Online!!"))
    print(f"logged {bot.user}" , (datetime.now().strftime("%x : %X")))
    bot.load_extension('cpuinfo')
    bot.load_extension('help')
    bot.load_extension('1')
    bot.load_extension('covid')
    bot.load_extension('kom')
    bot.load_extension('XXX')
    
    

    
    


@bot.command(brief="latency", help="พิม+ping เพื่อดูปิง")
async def ping(ctx):
    await ctx.send(f"ปิง {ctx.bot.latency * 1000:,.0f} ms")






@bot.command(aliases=['tr'],brief="แปลภาษา" ,help="พิม+tr แล้วตามด้วยภาษาที่ต้องการ แล้วก็ข้อความที่ต้องการแปล")
async def translate(ctx, lang_to, *args):
    """
    Translates the given text to the language `lang_to`.
    The language translated from is automatically detected.
    """

    lang_to = lang_to.lower()
    if lang_to not in googletrans.LANGUAGES and lang_to not in googletrans.LANGCODES:
        raise commands.BadArgument("Invalid language to translate text to")

    text = ' '.join(args)
    translator = googletrans.Translator()
    text_translated = translator.translate(text, dest=lang_to).text
    await ctx.send(text_translated)



#@bot.command()                                                                             #help Start
#async def help(ctx) :
    #print (f"commands +help request by {ctx.author}" , (datetime.datetime.now().strftime("%x : %X")))
    #cols = (0x32a852, 0x3296a8, 0xb700ff, 0x9232a8, 0xa8326f, 0xf25207, 0x3efa00, 0xfa0000)
    #emBed = discord.Embed(
        #title = "----------------------------------------คำสั่ง---------------------------------------",
        #color = random.choice(cols)
    #)
    #emBed.add_field(name="+help", value="ช่วยคนโง่ๆ", inline=True)
    #emBed.add_field(name="แขนขวา", value="สักทรงองค์นารายณ์", inline=True)
    #emBed.add_field(name="แขนซ้าย", value="สักชาติราชสีห์", inline=True)
    #emBed.add_field(name="ขาขวา", value="หมึกสักพยัคฆ์ภี", inline=True)
    #emBed.add_field(name="ขาซ้าย", value="สักหมีมีกำลัง", inline=True)
    #emBed.add_field(name="ฝันดี", value=":heart_eyes: ฝันดีคะ :heart_eyes:", inline=True)
    #emBed.add_field(name="การใช้บอทเพลง", value="How to use music bot?", inline=False)
    #emBed.add_field(name="+connect,+join", value="เชิญบอทเข้า", inline=True)
    #emBed.add_field(name="+play,+p", value="เลือกเพลงกดemoteข้างล่าง", inline=True)
    #emBed.add_field(name="+now play,+np", value="ดูเพลงที่เล่นอยู่", inline=True)
    #emBed.add_field(name="+pause", value="หยุดเพลง", inline=True)
    #emBed.add_field(name="+skip,+s", value="ข้ามเพลง", inline=True)
    #emBed.add_field(name="+repeat,+loop", value="พิมแล้วตามด้วย เปิด= loop enable | ปิด= loop disable", inline=True) 
    #emBed.add_field(name="+queue,+q,+playlist", value="ดูคิวเพลง", inline=True)
    #emBed.add_field(name="+shuffle,+สุ่ม", value="สุ่มเพลงในคิว", inline=True)
    #emBed.add_field(name="+previous", value="เล่นเพลงที่แล้ว", inline=True)
    #emBed.add_field(name="+leave,+dc", value="เตะน้องบอทออก:sob:", inline=True)
    #emBed.add_field(name="+server", value="server info", inline=True)
    #emBed.add_field(name="+XO", value= "พิม +XO แล้วแท็ก2คนเพื่อเล่น",inline=True)
    #emBed.add_field(name="+ลง", value= "พิม +ลง ตามด้วยเลข",inline=True)
    #emBed.add_field(name="ตารางตัวเลข", value= "[1, 2, 3]\n[4, 5, 6]\n[7, 8, 9]",inline=False)
    #emBed.add_field(name="ใช้บอทเล่นเกม", value= "ACTIVITIES",inline=False)
    #emBed.add_field(name="play poker", value="เล่น poker", inline=True)
    #emBed.add_field(name="play youtube", value="เปิดคลิป youtube", inline=True)
    #emBed.add_field(name="play betrayal", value="เล่น among us", inline=True)
    #emBed.add_field(name="play fishing", value="เล่นเกมตกปลา", inline=True)
    #emBed.add_field(name="+restart", value="รีบอททุกคำสั่ง(เพลงหาย)", inline=True)


    #await ctx.channel.send(embed=emBed)                                                    #help End



@bot.command(aliases=['out'] ,brief="คำสั่งต้องห้าม" ,help="คำสั่งต้องห้าม")
async def ตายซะ(ctx):
    yourID = 548777470829133824
    if ctx.message.author.id == yourID :
        await ctx.channel.send("เฮือก")
        await bot.change_presence(status=discord.Status.offline)
        await bot.logout()
    else:
        await ctx.channel.send('พวกเด็กกระโปกใช้คำสั่งนี้ไม่ได้หรอก')




@bot.event                                                                    #Q&A Start
async def on_message(message): 
    if message.content == "แขนขวา":
        await message.channel.send("สักทรงองค์นารายณ์")
    elif message.content == "เเขนขวา":
        await message.channel.send("สักทรงองค์นารายณ์")
    elif message.content == "แขนซ้าย":
        await message.channel.send("สักชาติราชสีห์")
    elif message.content == "เเขนซ้าย":
        await message.channel.send("สักชาติราชสีห์")
    elif message.content == "ขาขวา":
        await message.channel.send("หมึกสักพยัคฆ์ภี")
    elif message.content == "ขาซ้าย":
        await message.channel.send("สักหมีมีกำลัง")
    elif message.content == "เขาไม่เอามึงหรอก":
        await message.channel.send(":rage:แม่มึงสิ:rage:")
    elif message.content == "ฝันดี":
        await message.channel.send(":heart_eyes: ฝันดีคะ :heart_eyes:")
    elif message.content == "reminder_help":
        await message.channel.send("โปรดพิมคำสั่ง +reminder แลัวตามด้วยเวลา เช่น 5นาทีคือ 5m แล้วตามด้วยจะให้เตือนอะไรเช่น +reminder 5m เงี่ยน")
    elif message.content == "+help":
        await message.channel.send("ลอง +help1 +help2")
    await bot.process_commands(message)                                                                 #Q&A end

@bot.command(brief="ดูข้อมูล server discord" , help="พิม+server เพื่อดูข้อมูลดิส")                                                              #server info start
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + "server information",
        description=description,
        color=discord.Color.red())
    
    embed.set_thumbnail(url=icon)
    embed.add_field(name='owner', value=owner, inline=True)
    embed.add_field(name='server id', value=id, inline=True)
    embed.add_field(name='region', value=region, inline=True)
    embed.add_field(name='member count', value=memberCount, inline=True)

    await ctx.send(embed=embed)                                             #server info end




player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@bot.command(aliases=['Xo','XO','xo','xO'],brief="เล่นXO" ,help="พิม+xo แล้วแท็คเรา กับเพื่อน อีกคนเช่น +xo @a @b")
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    BotID = 840360664924422216
    if ctx.message.mentions[0].id == BotID:
        await ctx.channel.send("มีแต่พวกกากเท่านั้นที่เล่นกับบอท")
        return
    else:
        global count
        global player1
        global player2
        global turn
        global gameOver

        if gameOver:
            global board
            board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                    ":white_large_square:", ":white_large_square:", ":white_large_square:",
                    ":white_large_square:", ":white_large_square:", ":white_large_square:"]
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
                await ctx.send("ตาของ <@" + str(player1.id) + ">")
            elif num == 2:
                turn = player2
                await ctx.send("ตาของ <@" + str(player2.id) + ">")
        else:
            await ctx.send("เกมกำลังเริ่มอยู่เล่นให้จบก่อน")

@bot.command(alaises=['ลง'],brief="ลง XO" ,help="พิมลงแล้วตามด้วเลข \nตารางเลข\n1,2,3\n4,5,6\n7,8,9")
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
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
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
                    await ctx.send(mark + " ชนะ!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("เสมอ")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("ลงเลข1-9เท่านั้น")
        else:
            await ctx.send("ไม่ใช่ตามึง")
    else:
        await ctx.send("เริ่มเกมโดยใช้คำสั่ง+xo")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("แท็ก2คนเพื่อเล่น")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("error")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("ลง")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("ใส่เลข1-9")                                                            #XO command end





@bot.command(case_insensitive = True, aliases = ["remind", "remindme", "remind_me"])
@commands.bot_has_permissions(attach_files = True, embed_links = True)
async def reminder(ctx, time, *, reminder):
    print(f"ถูกใช้เตือนโดย{ctx.author}ในเวลา {time}")
    print(f"เรืองที่เตือน{reminder}")
    target = ctx.author
    user = ctx.message.author
    embed = discord.Embed(color=0x55a7f7, timestamp=datetime.utcnow())
    embed.set_footer(icon_url=f"{target.avatar_url}")
    seconds = 0
    if reminder is None:
        embed.add_field(name='Warning', value='โปรดใส่สิ่งที่ต้องการให้เตือน') # Error message
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} days"
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hours"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minutes"
    elif time.lower().endswith("s"):
        seconds += int(time[:-1])
        counter = f"{seconds} seconds"
    if seconds == 0:
        embed.add_field(name='Warning',
                        value='พิม reminder_help เพื่อดูวิธีใช้คำสั่ง')
    elif seconds < 60:
        embed.add_field(name='Warning',
                        value='ใส่เวลาอย่างน้อย1นาที')
    elif seconds > 7776000:
        embed.add_field(name='Warning', value='บอทกูไม่เปิดนานขนาดนั้นหรอก')
    else:
        embed.set_thumbnail(url=target.avatar_url)
        await ctx.send(f"เตือนให้ {reminder} ในอีก {counter}.")
        
        await asyncio.sleep(seconds)
        
        embed.set_thumbnail(url=target.avatar_url)
        embed.add_field(name= "เตือนแล้วนะ",
                        value= f"อย่าลีม {reminder} {ctx.author.mention}")
        await ctx.send(embed=embed)
        
        return
    await ctx.send(embed=embed)

@bot.command()
async def devmode(ctx, mode: int): 
    if mode == 1:
        await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing, name="Dev Time"))
        await ctx.send("Devmode On")
    elif mode == 2:
        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="Online!!"))
        await ctx.send("Devmode Off")
        
        
#for filename in os.listdir('./cogs'):
    #if filename.endswith('.py'):
        #bot.load_extension(f'cogs.{filename[:-3]}')





bot.run("Tokeng")                       #Token
