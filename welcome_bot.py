import discord
# docs == https://discordpy.readthedocs.io/en/stable/index.html

TOKEN = 'TOKEN'

client = discord.Client(activity=discord.Game(name='programming stuff'))

@client.event
async def on_ready():
    print("bot logged in as {0.user}".format(client))


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Hi {member.name}, welcome to ghostdragon_0")

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content).lower()
    channel = str(message.channel.name)

    if message.author == client.user:
        return

    if message.channel.name == 'general':
        if user_message == 'hi' or user_message == 'hello':
            await message.channel.send(f'Hello there, {username}')
            return
        if user_message == 'bye':
            await message.channel.send(f'see you later, {username}')
            return

client.run(TOKEN)
