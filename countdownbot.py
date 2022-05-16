import discord
import os
import asyncio
from discord.ext import commands, tasks
from datetime import datetime, timedelta
client = discord.Client()
TOKEN = 'TOKEN'
CHANNEL_ID = CHANNEL_ID
days_until_move_in = 99 #reset at: [127, 110, 99]

def seconds_until_midnight():
    now = datetime.now()
    target = (now + timedelta(days=0)).replace(hour=21, minute=0, second=0, microsecond=0)
    diff = (target - now).total_seconds()
    print(f"{target} - {now} = {diff}")
    return diff


@tasks.loop(hours=24)
async def called_once_a_day_at_midnight():
    global days_until_move_in
    await asyncio.sleep(seconds_until_midnight())
    message_channel = client.get_channel(CHANNEL_ID)
    print(f"Got channel {message_channel}")
    # added in the if statement on day 99
    if days_until_move_in == 1:
        await message_channel.send("MOVE IN IS TOMORROW!!! QUEER MINES CLASS OF 2026 ASSEMBLE!!!")
    elif days_until_move_in == 0:
        await message_channel.send("HAPPY MOVE IN DAY!!!")
    else:
        await message_channel.send(str(days_until_move_in) + " days until move in!")
    days_until_move_in -= 1

@called_once_a_day_at_midnight.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")

client = discord.Client()
called_once_a_day_at_midnight.start()
client.run(TOKEN)