import time
import random
import re

async def uwu_insult(message):
    insults = [
        "thou abominable hasty-witted whore-master",
        "thou base full-gorged horn-beast!",
        "thou beggarly pox-marked eunuch!",
        "thou beggarly tallow-faced mumble-news",
        "thou craven white-livered pumpion!",
        "thou dankish clay-brained mumble-news!",
        "thou dankish fly-bitten wagtail!",
        "thou errant dizzy-eyed slug!",
        "thou errant rude-growing flirt-gill!",
        "thou fawning ill-nurtured haggard!",
        "thou frothy muddy-mottled bitch-wolf!",
        "thou goatish elf-skinned promise-breaker",
        "thou gorbellied guts-griping harpy!",
        "thou lascivious beetle-headed foot-licker!",
        "thou pragging base-court measle!",
        "thou pragging tardy-gaited flirt-gill!",
        "thou rancorous pottle-deep tyrant!",
        "thou sanctimonious hasty-witted puttock!",
        "thou saucy clay-brained ruinous-butt!",
        "thou slanderous tardy-gaited pignut!",
        "thou soulless hasty-witted bum-bailey!",
        "thou soulless weather-bitten vassal!",
        "thou spleeny toad-spotted devil-incarnate",
        "thou surly tickle-brained gudgeon!",
        "thou unmuzzled hell-hated pigeon-egg!",
        "thou unwholesome idle-headed minnow!",
        "thou unwholesome milk-livered horse-dren",
        "thou venomed fly-bitten malt-horse!",
        "thou viperous decayed nut-hook!",
        "thou viperous guts-griping execrable-wretc",
        "thou withered flap-mouthed foul deformity"
    ]
    insult = random.choice(insults)
    if(len(message.content.lower().split(' ')) > 2):
        await message.channel.send(message.content.lower().split(' ')[2] + ", " + insult)
    else:
        await message.channel.send("Insult whom? You're a fucking idiot " + message.author.mention + " for not telling me whom to insult, good enough?")
    pass

async def uwu_dance(message):
    msg = await message.channel.send("Only for you, baby")
    time.sleep(1.5)
    for i in range(8):
        time.sleep(0.5)
        await msg.edit(content = 'Only for you, baby\n♪┏( UwU)┛♪')
        time.sleep(0.5)
        await msg.edit(content = 'Only for you, baby\n♪┗( UwU)┓♪')
    time.sleep(0.5)
    await msg.edit(content = 'Only for you, baby\n♪ ( UwU) ♪\nThat will be 50 bucks')
    pass


async def uwu_help(message):
    helpEmbed = discord.Embed(title = "Who's my little baby?")
    helpEmbed.add_field(name = "What I can do?", value = """
**UwU multiattack** - made to speed up rolling dice.
**UwU multiroll** - made for rolling many pacts of dice at once.
**UwU insult** - made for the good hearted of us.
**UwU roll** - made for when Avery (*the lil' bitch*) is down.
**UwU help** - made for babies like you.
**UwU say** - made so that you can make me your bitch, daddy.
**UwU dance** - made for sick fucks that like them hips move.
""", inline = False)
    helpEmbed.add_field(name = "UwU", value = "awr X3 *nuzzles* How are you? *pounces on you* you're so warm o3o *notices you have a bulge* someone's happy! *nuzzles your necky wecky* ~murr~ hehe ;) *rubbies your bulgy wolgy* you're so big! *rubbies more on your bulgy wolgy* it doesn't stop growing .///. *kisses you and licks your neck* daddy likes ;)")
    await message.channel.send(embed = helpEmbed)




async def uwu_respond(message):
    new_str = ""
    for sub_str in message.content.split(' ')[2:]:
        new_str += sub_str + " "
    if(new_str == ""):
        await message.channel.send("Say what, lil' bitch?")
    else:
        lst = list(new_str)
        lst[0]=new_str[0].upper()
        new_str = ''.join(lst)
        await message.channel.send(new_str + ", UwU")
