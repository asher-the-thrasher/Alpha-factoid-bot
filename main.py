# A Discord bot for the Alpha Gaming discord
# Contributors: Asher_The_Thrasher, Goldeneyes, Awkward Potato, Spartichaos
import os

import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, MissingAnyRole

from utils.keep_alive import keep_alive

from editable.config import configure
bot_activity=configure.bot_activity 
command_prefix=configure.command_prefix
Muted_role=configure.Muted_role
guild_id=configure.guild_id
from cogs.bot_raid_prevention import RaidProt


from cogs.mute import UnMuteCog

from replit import db
from discord_slash import SlashCommand



# secret bot token
token = os.environ['token']
intents = discord.Intents().all()
client = commands.Bot(command_prefix=command_prefix, intents=intents,case_insensitive= True,strip_after_prefix=True)
slash = SlashCommand(client, sync_commands=True)


# import cogs
for file in os.listdir("cogs"):
    if file.endswith(".py"):

        client.load_extension(f"cogs.{file[:-3]}")

client.load_extension(f"editable.config")


@client.event
async def on_ready():
    names = ""
    try:
        members = (await client.application_info()).team.members
        for member in members: 
            names = f"{names}, {member}"
    except:
        names = client.owner
    
    print(f'We have logged in as {client.user} which is in {str(len(client.guilds))} guilds whose prefix is {command_prefix} owned by {names}')
    
    activity = discord.Activity(name=bot_activity, type=discord.ActivityType.listening)
    await client.change_presence(activity=activity)
    
    UnMuteCog.doThisEveryTenSeconds.start(UnMuteCog, client)
    RaidProt.user_join_reset.start(RaidProt)
    await RaidProt.writing_to_users_joined(users_joined=0,mods_warned=0,users_banned = 0,banlock = 0)


@client.event
async def on_command_error(ctx, error):

    if isinstance(error, CommandNotFound):
        return
    if isinstance(error, MissingAnyRole):
        await ctx.send('You do not have permissions to use that command')
        return
    else:
        channel= await client.fetch_channel(894977926523666482)
        await channel.send(f"An error has occured in the bot\n\n {error}")
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
