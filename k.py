token = ""
boom = "" #Change ton prefix si tu parle pas anglais fils de pute 

preg = {
    "-fuuu": "(╯°□°）╯︵ ┻━┻",
    "-chomage": "https://gyazo.com/cd41d3f3c5bf09ac6a5b243b0a95b30d",
    "-run": "ᕕ( ᐛ )ᕗ",
    "-cool": "_へ__(‾◡◝ )>",
    "-uh": "(;¬_¬)",
    "-bc": "(҂⌣̀_⌣́)",
    "-gr": "(╬⓪益⓪)",
    "-wtf": " ͠° ͟ ͟ʖ ͡°",
    "-lenny": "(▀ ͜ʖ ͡°)",
    "-army": "( ͡° ͜ʖ ( ͡° ͜ʖ ( ͡° ͜ʖ ( ͡° ͜ʖ ͡°) ͜ʖ ͡°)ʖ ͡°)ʖ ͡°)",
    "-yes": "(•̀ᴗ•́)و ̑̑",
    "-yey": "( ͡° ͜ʖ ͡°)",
    "-idk": "¯\_(ツ)_/¯",
    "-wut": "ಠ_ಠ",
    "-bitch": "(⌐■_■)",
    "-issou": "https://www.tenor.co/N23D.gif",
    "-twitter": "https://twitter.com/KiruaBMO",
    "-fb": "https://www.facebook.com/KiruaLaDetaille",
    "-snap": "**:ghost: SNAP: skirua**",
    "-maroc": "https://tenor.com/view/morocco-gif-10654888",
    "-ytb": "https://www.youtube.com/channel/UCopJeFcYCYtJUqBUFeGvueA",
    "-pb": "https://pastebin.com/u/Empereur_Kirua",
    "-vespa": "https://discord.gg/hPMeHph",
    "-github": "**Github: **https://github.com/sKirua/",
    "-slime": "༼ つ ◕_◕ ༽つ ",

}

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import aiohttp
from random import choice
import random
import giphypop
import math
import urllib.parse
import re
import logging
import json



client = discord.Client()

def embed_perms(message):
    try:
        check = message.author.permissions_in(message.channel).embed_links
    except:
        check = True

print ("Veuillez patienter capitaine")

bot = commands.Bot(command_prefix=boom, self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
	print("										")
	print("	.▄▄ · ▄▄▄ .▄▄▌  ·▄▄▄▄▄▄▄·       ▄▄▄▄▄  ")
	print("	▐█ ▀. ▀▄.▀·██•  ▐▄▄·▐█ ▀█▪▪     •██    ")
	print("	▄▀▀▀█▄▐▀▀▪▄██▪  ██▪ ▐█▀▀█▄ ▄█▀▄  ▐█.▪  ")
	print("	▐█▄▪▐█▐█▄▄▌▐█▌▐▌██▌.██▄▪▐█▐█▌.▐▌ ▐█▌·  ")
	print("	 ▀▀▀▀  ▀▀▀ .▀▀▀ ▀▀▀ ·▀▀▀▀  ▀█▄▀▪ ▀▀▀   ")
	print("\n")
	print("Pseudo du capitaine: ",bot.user, "\n")
	print("Bot Developpé par Kirua")


@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        for k, v in preg.items():
            if k in msg.content:
                await bot.edit_message(msg, msg.content.replace(k, v))

    await bot.process_commands(msg)
@bot.command(pass_context=True)
async def clear(ctx, lol=0):
    t = int(lol) or 800
    if ctx.message.author.id == bot.user.id:
        async for m in bot.logs_from(ctx.message.channel,limit=t):
            if m.author.id == bot.user.id:
                try:
                    await bot.delete_message(m)
                except:
                    pass

@bot.command(pass_context=True)
async def ripinpeace(ctx):
    if bot.user.id == ctx.message.author.id:
        for user in list(ctx.message.server.members):
            try:
                await bot.ban(user)
                print (user.name + ", bouge de là mek")
            except:
                pass
        print ("Done : ripinpeace")
        await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def avatar(ctx, url):
    if bot.user.id == ctx.message.author.id:
        async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    data = await r.read()
    await bot.edit_profile(password="", avatar=data)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def rainbow(ctx, lawl:int, mamacita:str):
    rainbow = await bot.say(embed=discord.Embed(title=mamacita, color=discord.Color.red()))
    sex = 0
    await bot.delete_message(ctx.message)
    while lawl > sex:
        sex = sex + 1
        color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        color = int(color, 16)
        await bot.edit_message(rainbow, embed=discord.Embed(title=mamacita, color=discord.Color(value=color)))
        await asyncio.sleep(1)

@bot.command(pass_context=True)
async def a(ctx, mamacita:str):
    if bot.user.id == ctx.message.author.id:
        color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        color = int(color, 16)
        await bot.say(embed=discord.Embed(title=mamacita, color=discord.Color(value=color)))
        await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def getav(ctx, user: discord.Member):
    if bot.user.id == ctx.message.author.id:
        u = user.avatar_url
    embed=discord.Embed(title="Voici la pdp du macaque nomé " + user.name, color=0x9900FF)
    embed.set_image(url=u)
    await bot.say(embed=embed)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def twitter(ctx):
    embed=discord.Embed(title="Twitter",url="https://twitter.com/KiruaBMO", color=0x9900FF 	)
    embed.set_thumbnail(url="https://i.imgur.com/vuIsHwf.png")
    embed.add_field(name="KiruaBMO", value="Follow moi si tu tient à la vie.", inline=False)
    await bot.say(embed=embed)
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def cyao(ctx):
    if bot.user.id == ctx.message.author.id:
        for emoji in list(ctx.message.server.emojis):
            try:
                await bot.delete_custom_emoji(emoji)
            except:
                pass
        for channel in list(ctx.message.server.channels):
            try:
                await bot.delete_channel(channel)
            except:
                pass
        for role in list(ctx.message.server.roles):
            try:
                await bot.delete_role(ctx.message.server, role)
            except:
                pass
        for user in list(ctx.message.server.members):
            try:
                await bot.ban(user)
            except:
                pass

@bot.command(pass_context=True)
async def ombre(ctx):
    await bot.say("\n".join(["```fix",

"                 &%                                        ",
"             &    %%%%.                                    ",
"            &@    @@@&%%%%%/*                              ",
"          //     @@@@                                      ",
"            &&  &&&&&&&.                (@@@/              ",
"           #&&&   &&&&&&&&&  /%&@@@@@@@@@@@@@ @@           ",
"          &&&&.  /&&&&&&&&& @@@@@@@@@@@@@@@@@@@@           ",
"          #&&&   &&&&&&&&&% @@@@@@@@@@@@@@@@@@@@           ",
"         #&&&    &&&&&&&&&   &&&&&&&%%%%%%%%%%%%           ",
"         &&&&    &&&&&&&&&   %&&&&%%%%%%%% %%%%%&&&        ",
"         &&&     &&&&&&&&&   &&&&&&&&%%% %%%%&&&&&&&&      ",
"         && //. &&&&&&&&&&  %%%&&&&&&&% %%%%&&&&&&&&&&     ",
"         && ./  &&&&&&&&&&  %%%&&&&&&&%#%%%&&&&&&&&&&&&    ",
"        .%%%%%@&&&&&&&&&&&& %%%&&&&&&&%%%%%&&&&&&&&&&&&    ",
"   % &%%%%%%%%%%%@&&&&&&&&&&/%%&&&&&&&%,%%%&&&&&&&&&&&&.   ",
" %%%%%%%%%&&&&&&&&&@&&&&&&&& %&&&&&&&&% %%%%&&&&&&&&%      ",
"%%%%%%%%%&&&&&&&&&&&&@&&&&&&&&&&&&&&%%%% %%%(   @*         ",
"@@@@%%%%%%&&&&&&&&&&&@&&&&&&&&%%%%%% & & #. % / @#         ",
"    @@@.        @&&&&&@&&&&&&&&,*@ @  %@@@ #.  @@          ",
"  .@@@  @@@@@@@  @@&&&                  @@@ @@@@  @        ",
"  @@@& @..   @@@                         @@@     @         ",
" #@@@  ..     @@                           @@@@&           ",
" @@@@ ,.   /, @@                                           ",
" #@@@  ..    @@@                                           ",
"  @@@@ @....@@@  %                                         ",
"   @@@*  @@@@   @                                          ",
"    @@@@      *.                                           ",
"      @@@@@@@"
"                                             ",
"                    root@vespa~#python k.py",
"                   1337 haxor in da place        ",


    "```"]))
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def help(ctx, *, name=""):
    embed=discord.Embed(title="𝑳𝒊𝒔𝒕𝒆𝒔 𝒅𝒆𝒔 𝒄𝒐𝒎𝒎𝒂𝒏𝒅𝒆𝒔 𝒅𝒖 𝑺𝒆𝒍𝒇𝒃𝒐𝒕 𝒅𝒆 𝒍𝒂 𝑽𝒆𝒔𝒑𝒂.",color=0x9900FF)
    embed.add_field(name='𝐜𝐥𝐞𝐚𝐫', value='𝐕𝐨𝐮𝐬 𝐩𝐞𝐫𝐦𝐞𝐭𝐬 𝐝𝐞 𝐬𝐮𝐩𝐩𝐫𝐢𝐦𝐞𝐫 𝐭𝐨𝐮𝐭 𝐯𝐨𝐬 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬 𝐨𝐮 𝐮𝐧 𝐧𝐨𝐦𝐛𝐫𝐞 𝐬𝐩𝐞́𝐜𝐢𝐟𝐢𝐪𝐮𝐞 𝐝𝐞 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬', inline=False)
    embed.add_field(name='𝐚', value='𝐕𝐨𝐮𝐬 𝐩𝐞𝐫𝐦𝐞𝐭𝐬 𝐝𝐞 𝐟𝐚𝐢𝐫𝐞 𝐝𝐞𝐬 𝐞𝐦𝐛𝐞𝐝', inline=False)
    embed.add_field(name='𝐭𝐰𝐢𝐭𝐭𝐞𝐫', value='𝐀𝐟𝐟𝐢𝐜𝐡𝐞 𝐮𝐧 𝐞𝐦𝐛𝐞𝐝 𝐚𝐯𝐞𝐜 𝐯𝐨𝐭𝐫𝐞 𝐓𝐰𝐢𝐭𝐭𝐞𝐫 [𝐜𝐡𝐚𝐧𝐠𝐞𝐳 𝐝𝐚𝐧𝐬 𝐥𝐚 𝐬𝐨𝐮𝐫𝐜𝐞]', inline=False)
    embed.add_field(name='𝐜𝐲𝐚𝐨', value='𝐅𝐚𝐢𝐭 𝐜𝐞𝐭𝐭𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐞 𝐬𝐮𝐫 𝐭𝐨𝐧 𝐩𝐫𝐨𝐩𝐫𝐞 𝐝𝐢𝐬𝐜𝐨𝐫𝐝 𝐬𝐢 𝐭 𝐮𝐧 𝐡𝐨𝐦𝐦𝐞', inline=False)
    embed.add_field(name='𝐎𝐦𝐛𝐫𝐞', value='𝐂𝐞𝐭𝐭𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐞 𝐟𝐚𝐢𝐭 𝐝𝐞 𝐭𝐨𝐢 𝐮𝐧 𝐩𝐢𝐫𝐚𝐭𝐞', inline=False)
    embed.add_field(name='𝐥𝐢𝐯𝐞', value='𝐂𝐞𝐭𝐭𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐞 𝐜𝐡𝐚𝐧𝐠𝐞 𝐯𝐨𝐭𝐫𝐞 𝐬𝐭𝐚𝐭𝐮𝐭', inline=False)
    embed.add_field(name='𝐞𝐜𝐨𝐮𝐭𝐞', value='𝐂𝐞𝐭𝐭𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐞 𝐜𝐡𝐚𝐧𝐠𝐞 𝐯𝐨𝐭𝐫𝐞 𝐬𝐭𝐚𝐭𝐮𝐭)', inline=False)
    embed.add_field(name='𝐰𝐚𝐭𝐜𝐡', value='𝐂𝐞𝐭𝐭𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐞 𝐜𝐡𝐚𝐧𝐠𝐞 𝐯𝐨𝐭𝐫𝐞 𝐬𝐭𝐚𝐭𝐮𝐭)', inline=False)
    embed.add_field(name='𝐣𝐨𝐮𝐞', value='𝐂𝐞𝐭𝐭𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐞 𝐜𝐡𝐚𝐧𝐠𝐞 𝐯𝐨𝐭𝐫𝐞 𝐬𝐭𝐚𝐭𝐮𝐭)', inline=False)
    embed.add_field(name='𝐧𝐨𝐨𝐛', value='𝐏𝐞𝐫𝐦𝐞𝐭𝐬 𝐝𝐞 𝐫𝐞́𝐩𝐨𝐧𝐝𝐫𝐞 𝐚𝐮 𝐪𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐝𝐞𝐬 𝐧𝐨𝐨𝐛', inline=False)
    embed.add_field(name='𝐧𝐢𝐜𝐤𝐧𝐚𝐦𝐞 + 𝐩𝐬𝐞𝐮𝐝𝐨 ', value='𝐂𝐡𝐚𝐧𝐠𝐞 𝐯𝐨𝐭𝐫𝐞 𝐩𝐬𝐞𝐮𝐝𝐨 𝐬𝐮𝐫 𝐥𝐞𝐬 𝐬𝐞𝐫𝐯𝐞𝐮𝐫𝐬', inline=False)
    embed.add_field(name='𝐪𝐢 + @𝐦𝐚𝐜𝐚𝐪𝐮𝐞 ', value='𝐂𝐚𝐥𝐜𝐮𝐥 𝐥𝐞 𝐪𝐢 𝐝\'𝐮𝐧 𝐦𝐚𝐜𝐚𝐪𝐮𝐞',inline=False)
    embed.add_field(name='𝐮𝐬𝐞𝐫𝐢𝐧𝐟𝐨 + @𝐦𝐚𝐜𝐚𝐪𝐮𝐞 ', value='𝐏𝐞𝐫𝐦𝐞𝐭𝐬 𝐝𝐞 𝐭𝐨𝐮𝐭 𝐬𝐚𝐯𝐨𝐢𝐫 𝐬𝐮𝐫 𝐮𝐧 𝐦𝐚𝐜𝐚𝐪𝐮𝐞', inline=False)
    embed.set_thumbnail(url='https://i.imgur.com/GxNI0Mk.png')
    embed.set_author(name='𝐕𝐞𝐬𝐩𝐚 𝐂𝐨𝐫𝐩𝐨𝐫𝐚𝐭𝐢𝐨𝐧', icon_url='https://i.imgur.com/GxNI0Mk.png')
    embed.set_image(url='https://i.imgur.com/W1ZFZ3h.gif')
    embed.set_footer(text='◊ Copyright © 2018 𝐕𝐞𝐬𝐩𝐚 𝐂𝐨𝐫𝐩𝐨𝐫𝐚𝐭𝐢𝐨𝐧 Project. ◊')
    await bot.say(embed=embed)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def live(ctx):
    if bot.user.id == ctx.message.author.id:
        await bot.change_presence(game=discord.Game(name="𝐕𝐞𝐬𝐩𝐚 𝐂𝐨𝐫𝐩𝐨𝐫𝐚𝐭𝐢𝐨𝐧 𝐕𝟐.𝟎", url="https://twitch.tv/skiruaa", type=1))
    await bot.delete_message(ctx.message)
    
@bot.command(pass_context=True)
async def ecoute(ctx):
    if bot.user.id == ctx.message.author.id:
        await bot.change_presence(game=discord.Game(name="tout ce que tu dit.", url="https://twitch.tv/skiruaa", type=2))
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def watch(ctx):
    if bot.user.id == ctx.message.author.id:
        await bot.change_presence(game=discord.Game(name="Le cul de ta soeur.", type=3))
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def joue(ctx):
    if bot.user.id == ctx.message.author.id:
        await bot.change_presence(game=discord.Game(name="", type=0))
    await bot.delete_message(ctx.message)
    
@bot.command(pass_context=True)
async def noob(ctx, *, msg: str):
        lmgtfy = 'http://lmgtfy.com/?q='
        await bot.say(lmgtfy + urllib.parse.quote_plus(msg.lower().strip()))
        await bot.delete_message(ctx.message)
        
@bot.command(pass_context=True)
async def ytb(ctx, *, msg: str):
        ytb = 'https://www.youtube.com/results?search_query='
        await bot.say(ytb + urllib.parse.quote_plus(msg.lower().strip()))
        await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def geo(ctx, *, msg: str):
        ip = 'https://www.ip-tracker.org/locator/ip-lookup.php?ip='
        await bot.say(ip + urllib.parse.quote_plus(msg.lower().strip()))
        await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def gif(ctx, *, msg: str):
        gif = 'https://giphy.com/search/'
        await bot.say(gif + msg.lower().replace(" ", "-") )
        await bot.delete_message(ctx.message)




bot.run(token, bot=False)
