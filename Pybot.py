import discord
from discord.ext.commands import Bot
from discord.ext import commands
import random

# creates a new Discord client
client = discord.Client()
token = '<your token goes here>'

# I know these words are dirty/offensive, but I had to add them in to make sure that users on the server aren't using bad language. 
chat_filter = ["DAMN", "FUCK", "SHIT", "ASS", "ANAL", "HELL", "VAGINA", "BOOBS"]
bypass_list = []

@client.event
async def on_ready():
    print(client.user.name, client.user.id, "is connected to Discord.")
    print('------')

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
                    await client.send_message(message.channel, "**FILTER FOR SEAN'S DIRTY MOUTH:** You aren't allowed to use that kind of language!")
                except discord.errors.NotFound:
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

    if message.content.startswith('!number'):
        num = random.randint(0, 100000)
        await client.send_message(message.channel, num)

    userID = message.author.id
    if message.content.startswith('!say'):
        #'<your ID>' = your ID
        if message.author.id == '<your ID>':
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You are not authorized!")

            # "<your Admin role ID>" = Admin role ID
            # I can't get this admin role checker to work... Maybe it isn't supposed to check for the role IDs.
            # trying to pass {0.author.mention}.format(message) into it but won't work.
    if message.content.upper().startswith('!AMIADMIN'):
        if "<your Admin role ID>" is (role.id for role in message.author.roles):
            await client.send_message(message.channel, "**ROLE CHECKER:** You are an admin of this server.")
        else:
            await client.send_message(message.channel, "**ROLE CHECKER:** You are not an admin of this server!")

    if message.content.startswith('!purge'):
        tmp = await client.send_message(message.channel, "Purging all of your messages from this channel...")
        async for msg in client.logs_from(message.channel):
            await client.delete_message(msg)
        if not message.author.id:
            await client.send_message(message.channel, "You don't have permission!")


           # other code here
        
client.run(token)
