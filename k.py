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
    print ("Paré à l'attaque capitaine.")

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
async def cmd(ctx):
    await bot.say("\n".join(["```fix",
"       __     __",
"       \ \   / /__  ___ _ __   __ _",
"        \ \ / / _ \/ __| '_ \ / _` |",
"         \ V /  __/\__ \ |_) | (_| |",
"          \_/ \___||___/ .__/ \__,_|",
"                        |_|",
" Tu fait parti de la cour des grands petit",
" Tu as mtn acces au selfbot privé de la vespa",
"                                                           ",
" 1) clear (Vous permets de supprimer tout vos messages ou un nombre spécifique de messages )",
"                                                           ",
" 2) ripinpeace (Vous permets de ban tout les utilisateurs d'un discord)",
"                                                           ",
" 3) avatar + url (Vous permets de changer d'avatar avec un lien)",
"                                                           ",
" 4) rainbow + texte (Vous permets de faire un embed qui change de coulleur avec un texte au choix) ",
"                                                           ",
" 5) a + texte (Vous permets de faire un embed avec une coulleur aléatoir) ",
"                                                           ",
" 6) getav @macaque_a_qui_tu_veux_voler_la_pdp (Vous permets de voler des avatar ou de vous moquer de l'avatar de vos camarades) ",
"                                                           ",
" 7) twitter (Affiche un embed avec votre Twitter [changez dans la source]",
"                                                           ",
" 8) cyao (fait cette commande sur ton propre discord si t un homme) ",
"                                                           ",
" 9) ombre (cette commande fait de vous un pirate) ",
"                                                           ",
" 10) live (cette commande vous affiche en stream) ",
    "```"]))
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




bot.run(token, bot=False)
