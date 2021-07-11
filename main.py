# A Discord bot that analyzes OBS log files for the Alpha Gaming discord
# Contributors: Asher_The_Thrasher, Goldeneyes, Awkward Potato, Spartichaos
import os
import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound
from utils.keep_alive import keep_alive
from editable.config import command_prefix
from editable.config import bot_activity

import json
from replit import db



# secret bot token
token = os.environ['token']
intents = discord.Intents.all()
client = commands.Bot(command_prefix=command_prefix, intents=intents)
#client.remove_command('help')

#import cogs
for file in os.listdir("cogs"):
  if file.endswith(".py"):
      client.load_extension(f"cogs.{file[:-3]}")



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Activity(name=bot_activity, type=discord.ActivityType.listening)
    await client.change_presence(activity=activity)
    #UnMuteCog.doThisEveryTenSeconds.start(UnMuteCog, client)
    channel = 849649811241173075
    


keys = db.keys()


"""with open('utils/commands.json') as json_file:
    commands_by_number = json.load(json_file)

factoids_by_name = {}

for command in commands_by_number.values():
    factoids_by_name[command["Command"]] = [{'name': command["Command"], 'content': command["Text"]}]
    name = command["Command"]
    content = command["Text"]
    db[name] = content

with open('utils/factoids.json', 'w') as out_file:
    json.dump(factoids_by_name, out_file, indent=2)
"""
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error
  


keep_alive()
client.run(token)
