import asyncio
import discord
from discord.ext.commands import Bot

# creates a new Discord client
client = discord.Client()
token = 'NDMxMjU5MjYyNzI4MjczOTMw.DacJtA.a4rVp5q8vIISkMzgcH9n7Oi5scE'
Client = Bot('!')

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

# bulk delete messages implementation
@Client.command(pass_context = True)
async def clear(ctx, number):
    mgs = [] # Empty list to put all the messages in the log
    number = int(number) # Converting the amount of messages to delete to an integer
    async for x in Client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await Client.delete_messages(mgs)
    
client.run(token)
