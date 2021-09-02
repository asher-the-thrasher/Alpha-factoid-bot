# A Discord bot for the Alpha Gaming discord
# Contributors: Asher_The_Thrasher, Goldeneyes, Awkward Potato, Spartichaos
import os

import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, MissingAnyRole

from utils.keep_alive import keep_alive

from editable.config import bot_activity
from editable.config import command_prefix

from cogs.mute import UnMuteCog

from replit import db
from editable.config import Muted_role
from editable.config import guild_id

from discord_slash import SlashCommand


# secret bot token
token = os.environ['token']
intents = discord.Intents().all()
client = commands.Bot(command_prefix=command_prefix, intents=intents)
slash = SlashCommand(client, sync_commands = True, sync_on_cog_reload = True,)

# import cogs
for file in os.listdir("cogs"):
    if file.endswith(".py"):
        if file == "factiod.py":
            continue

        client.load_extension(f"cogs.{file[:-3]}")

#@client.event
#async def on_component(ctx: ComponentContext):
  #print("recieved")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
    activity = discord.Activity(name=bot_activity, type=discord.ActivityType.listening)
    await client.change_presence(activity=activity)
    
    UnMuteCog.doThisEveryTenSeconds.start(UnMuteCog, client)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    if isinstance(error, MissingAnyRole):
        await ctx.send('You do not have permissions to use that command')
        return
    raise error


@client.event
async def on_member_join(member):
  try:
    member_id = member.id
    value = db[f"!?!?!?!? {member_id}"]
    
    if value is None:
      return
    
    guild = client.get_guild(guild_id)
    muted = guild.get_role(Muted_role)
    await member.add_roles(muted, reason="attempted mute evasion")
  except:
    return
    
keep_alive()
client.run(token)
