import discord
from discord.ext import commands
import random
import sys

# creates a new Discord client
client = discord.Client()
token = 'token'


@client.event
async def on_ready():
    print('Successfully logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!bot'):
        await client.send_message(message.channel, "Yes?")
    elif message.content.startswith('!flip'):
        flip = random.choice(['Heads!', 'Tails!'])
        await client.send_message(message.channel, flip)
    elif message.content.startswith('!color'):
        color = ['red', 'green', 'blue', 'orange', 'grey', 'purple', 'yellow', 'black', 'gold']
        randomized = random.choice(color)
        await client.send_message(message.channel, randomized)
        
client.run(token)
