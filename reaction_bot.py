import discord

TOKEN = "TOKEN"
client = discord.Client()


@client.event
async def on_ready():
    print("bot is loggeed in")


@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    role = None
    if message_id == MESSAGE_ID:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        print(payload.emoji.name)
        if payload.emoji.name == '✨':
            print("sparkles role")
            role = discord.utils.get(guild.roles, name='Sparkles')
        elif payload.emoji.name == '🌊':
            role = discord.utils.get(guild.roles, name='Ocean')

        if role is not None:
            member = await(await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
            if member is not None:
                await member.add_roles(role)
                print("done")
            else:
                print('member not odunf')


@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    role = None
    if message_id == MESSAGE_ID:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        print(payload.emoji.name)
        if payload.emoji.name == '✨':
            print("sparkles role")
            role = discord.utils.get(guild.roles, name='Sparkles')
        elif payload.emoji.name == '🌊':
            role = discord.utils.get(guild.roles, name='Ocean')

        if role is not None:
            member = await(await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
            if member is not None:
                await member.remove_roles(role)
                print("done")
            else:
                print('member not odunf')


client.run(TOKEN)
