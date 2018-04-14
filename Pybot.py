import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random

# creates a new Discord client
client = discord.Client()
token = '<token here>'

chat_filter = ["<a bunch of disturbing words here>"]
bypass_list = []

@client.event
async def on_ready():
    print(client.user.name, client.user.id, "is connected to Discord.")
    print('------')
    await client.change_status(game=discord.Game(name='<whatever goes here>'))

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "***CHAT FILTER:*** You aren't allowed to use that kind of language!  You have been warned!")
                except discord.errors.NotFound:
                    return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!bot'):
        await client.send_message(message.channel, "Need anything?  If so, type '!help'")

    if message.content.startswith('!flip'):
        flip = random.choice(['Heads!', 'Tails!'])
        await client.send_message(message.channel, flip)

    if message.content.startswith('!color'):
        color = ['red', 'green', 'blue', 'orange', 'grey', 'purple', 'yellow', 'black', 'gold']
        randomized = random.choice(color)
        await client.send_message(message.channel, randomized)

    if message.content.startswith('!number'):
        num = random.randint(0, 100000)
        await client.send_message(message.channel, num)
        
            # "<Admin ID here>" = Admin role ID
            # I can't get this admin role checker to work... Maybe it isn't supposed to check for the role IDs.
    if message.content.upper().startswith('!AMIADMIN'):
        if "<Admin role here>" is (role.id for role in message.author.roles):
            await client.send_message(message.channel, "**ROLE CHECKER:** You are an admin of this server.")
        else:
            await client.send_message(message.channel, "**ROLE CHECKER:** You are not an admin of this server!")

    # purge messages
    if message.content.startswith('!purge'):
        if message.author.id != '<your ID here>':
            try:
                await client.send_message(message.channel, "You aren't allowed access to this command!")
            except discord.errors.NotFound:
                return
        else:    
            tmp = await client.send_message(message.channel, "Purging messages from this channel...")
            async for msg in client.logs_from(message.channel):
                await client.delete_message(msg)
        
    # help command - prints a list of useful bot commands
    if message.content.startswith('!help'):
        file = open('commands.txt', 'r') # reads from commands.txt
        if file.mode == 'r':
            # read() function reads the contents
            contents = file.read()
            await client.send_message(message.channel, contents)

client.run(token)
