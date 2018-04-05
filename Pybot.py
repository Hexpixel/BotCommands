import discord

# creates a new Discord client
client = discord.Client()

@client.event
async def on_ready():
    print('Successfully logged in as')
    print('Username:', client.user.name)
    print('User ID:', client.user.id)
    print('------')

# New member
@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

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
        
client.run('token')

