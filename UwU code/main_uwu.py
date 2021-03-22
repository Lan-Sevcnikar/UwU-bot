import discord
import random
import re
import os
from uwu_dnd import uwu_roll, uwu_multiattack, uwu_multiroll
from uwu_rand import uwu_insult, uwu_help, uwu_respond, uwu_dance
import time

client = discord.Client()

# TO DO
    # insult generator https://evilinsult.com/generate_insult.php?lang=en&type=json
    # dancing 

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if(message.author == client.user):
        return
    if (message.content.split(' ')[0].lower() == 'uwu'):
        if(len(message.content.split(' ')) == 1):
            await message.channel.send('I need arguments, you fuwul')
        else:
            uwu_command = message.content.split(' ')[1].lower()
            if(uwu_command == 'help'):
                await uwu_help(message)
            elif(uwu_command == "multiattack"):
                await uwu_multiattack(message)
            elif(uwu_command == "multiroll"):
                await uwu_multiroll(message)
            elif(uwu_command == "roll"):
                await uwu_roll(message)
            elif(uwu_command == "insult"):
                await uwu_insult(message)
            elif(uwu_command == "say"):
                await uwu_respond(message)
            elif(uwu_command == 'dance'):
                await uwu_dance(message)
            elif(message.content.lower() == 'uwu shut up'):
                await message.channel.send("Make me, you bottom")
            else:
                await message.channel.send("I'm sowwy, I don't understand. Try *UwU help*")

client.run("ODA1NTAzMDMxMjUyMjIyMDQy.YBb1KA.peVuiSID7ck4eCzLfi7Q-FRJTtk")