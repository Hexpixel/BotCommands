import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random

# creates a new Discord client
client = discord.Client()
token = 'token'


@client.event
async def on_ready():
    print(client.user.name, client.user.id, "is connected to Discord.")
    print('------|------|------|------|------|------|------')

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!bot'):
        await client.send_message(message.channel, "Yes?")
    if message.content.startswith('!flip'):
        flip = random.choice(['Heads!', 'Tails!'])
        await client.send_message(message.channel, flip)
    if message.content.startswith('!color'):
        color = ['red', 'green', 'blue', 'orange', 'grey', 'purple', 'yellow', 'black', 'gold']
        randomized = random.choice(color)
        await client.send_message(message.channel, randomized)
    userID = message.author.id
    if message.content.upper().startswith('!SAY'):
        #'your ID' = my ID
        if message.author.id == 'your ID':
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You are not authorized!")
            # "your admin role" = Admin role ID
    if message.content.upper().startswith('!AMIADMIN'):
        if "your admin role" is (role.id for role in message.author.roles):
            await client.send_message(message.channel, "You are an admin")
        else:
            await client.send_message(message.channel, "You are not an admin")

            # other code for this specific if statement can go here please

client.run(token)
