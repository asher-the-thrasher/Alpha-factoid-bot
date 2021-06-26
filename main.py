# A Discord bot that analyzes OBS log files for the Alpha Gaming discord
# Contributors: Asher_The_Thrasher, Goldeneyes, Awkward Potato, Spartichaos
import os

import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, MissingAnyRole
from dotenv import load_dotenv

from editable.config import bot_activity
from editable.config import command_prefix

# secret bot token
load_dotenv()
token = os.environ['token']
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=command_prefix, intents=intents)

# import cogs
for file in os.listdir("cogs"):
    if file.endswith(".py"):
        if file == "factiod.py":
            continue

        client.load_extension(f"cogs.{file[:-3]}")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Activity(name=bot_activity, type=discord.ActivityType.listening)
    await client.change_presence(activity=activity)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    if isinstance(error, MissingAnyRole):
        await ctx.send('You do not have permissions to use that command')
        return
    raise error


#keep_alive()
client.run(token)
