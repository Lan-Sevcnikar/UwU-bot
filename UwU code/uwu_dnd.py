import time
import random
import re

async def uwu_roll(message):
    s = message.content.lower()
    cs = "uwu\s+roll\s+(?P<at_d_n>\d+)d(?P<at_d_s>\d+)(?P<at_d_mod>\s*[+,-]\d+)?"
    p = re.compile(cs)
    try:
        dn = int(p.match(s).group("at_d_n"))
        ds = int(p.match(s).group("at_d_s"))
        dm = 0
        if(p.match(s).group('at_d_mod')):
            dm = int(p.match(s).group('at_d_mod'))
        

        total = dm
        result = "**Result:** ("

        for die in range(dn):
            value = int(random.random()*ds+1)
            if(value == 1 or value == ds):
                result += "**"
            result += str(value)
            if(value == 1 or value == ds):
                result += "**"
            result += ","
            total += value
        result = result[0:-1]
        result += ")"
        if(p.match(s).group('at_d_mod')):
            result += (p.match(s).group('at_d_mod')).strip()
        #message.author.username + "\n" + 
        await message.channel.send(message.author.mention + "\n" + result + "\n" + "**Total**: " + str(total))

    except:
        await message.channel.send("UwU - That ain't gonna fly, pog champ\nx**d**y+z; where x,y,z are number of dice, how many sides they have and the roll modifier")
        pass


async def uwu_multiattack(message):
    s = message.content.lower()
    cs = "uwu\s+multiattack\s+(?P<num>\d+)(?P<at_mod>\s+[-,+]\d+)?\s+(?P<at_d_n>\d+)d(?P<at_d_s>\d+)(?P<at_d_mod>\s*[+,-]\d+)?\s+(?P<AC>\d+)"
    p = re.compile(cs)
    try:
        n = int(p.match(s).group("num"))
        m = 0
        mod_str = ""
        mob_str = ""
        if(p.match(s).group("at_mod")):
            mod_str = p.match(s).group("at_mod").strip()
            m = int(p.match(s).group("at_mod"))
        AC = int(p.match(s).group("AC"))
        dn = int(p.match(s).group("at_d_n"))
        ds = int(p.match(s).group("at_d_s"))
        dm = 0
        if(p.match(s).group('at_d_mod')):
            mod_str = p.match(s).group('at_d_mod').strip()
            dm = int(p.match(s).group('at_d_mod'))

        if(n <= 0 or dn <= 0 or ds <= 0):
            x = 1/0

        total_damadge = 0
        left_col = ""
        right_col = ""

        for i in range(n):
            attack = int(random.random()*20+1)
            if(attack == 20):
                temp = 2 * dn
                left_col += "(**{roll}**){mod} = **{summ}**\n".format(roll = attack, mod = mod_str, summ = attack + m)
            elif(attack == 1):
                left_col += "(**{roll}**){mod} = **{summ}**\n".format(roll = attack, mod = mod_str, summ = attack + m)
                right_col += "*miss*\n"
                continue
            else:
                left_col += "({roll}){mod} = **{summ}**\n".format(roll = attack, mod = mod_str, summ = attack + m)
                temp = dn
            attack += m
            
            damage = 0
            if(attack > AC):
                right_col += "("
                for j in range(temp):
                    dmd = int(random.random()*ds+1)
                    if(dmd == 1 or dmd == ds):
                        right_col += "**" + str(dmd) + "**,"
                    else:
                        right_col +=str(dmd) + ","
                    damage += dmd + dm
                right_col = right_col[0:-1] + ")" + mob_str + " = **" + str(damage) + "**\n"
            else:
                right_col += "*miss*\n"
            total_damadge += damage

        helpEmbed = discord.Embed(title = "UwU - multiattack", value = "Get wedy for a pawunding ^-^")
        helpEmbed.add_field(name = "To hit", value = left_col, inline = True)
        helpEmbed.add_field(name = "Damage", value = right_col, inline = True)
        helpEmbed.add_field(name = "Total damage", value = "**"+str(total_damadge)+"**", inline = False)

        await message.channel.send(embed = helpEmbed)
    except:
        await message.channel.send("UwU - That ain't gonna fly, pog champ\nn m x**d**y+z ac; where n is the number of attackers, m is the mod to hit, xfy+z the standard dice and AC AC")
        pass

async def uwu_multiroll(message):
    s = message.content.lower()
    cs = "uwu\s+multiroll\s+(?P<num>\d+)\s+(?P<at_d_n>\d+)d(?P<at_d_s>\d+)(?P<at_d_mod>\s*[+,-]\d+)?"
    p = re.compile(cs)
    try:
        n = int(p.match(s).group("num"))
        dn = int(p.match(s).group("at_d_n"))
        ds = int(p.match(s).group("at_d_s"))
        dm = 0
        if(p.match(s).group('at_d_mod')):
            dm = int(p.match(s).group('at_d_mod'))
        
        answer_thing = message.author.mention + "\n"
        total_total = 0
        
        for rollll in range(n):
            total = dm
            result = "Result: ("
            for die in range(dn):
                value = int(random.random()*ds+1)
                if(value == 1 or value == ds):
                    result += "**"
                result += str(value)
                if(value == 1 or value == ds):
                    result += "**"
                result += ","
                total += value
            result = result[0:-1]
            result += ")"
            if(p.match(s).group('at_d_mod')):
                result += (p.match(s).group('at_d_mod'))
            #message.author.username + "\n" + 
            total_total += total
            answer_thing += result + "\n" + "Total: " + str(total) + "\n"
        
        answer_thing +="**Total total**: " + str(total_total)
        await message.channel.send(answer_thing)

    except:
        await message.channel.send("UwU - That ain't gonna fly, pog champ\nn x**d**y+z; where n,x,y,z are number of batches, number of dice, how many sides they have and the roll modifier")
        pass