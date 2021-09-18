import discord
from discord.ext.commands import Cog,command,has_any_role
from editable.config import configure  
another_role=configure.another_role
bot_commander=configure.bot_commander
import os


class disabling_reenableing_cogs(Cog):
  def __init__(self, client):
    self.client = client
    self.asher = '<@691724738841804843>'
    self.tator = '<@334067992465899520>'
  @command()
  async def shutdown(self, ctx):
    try:
      await has_any_role(bot_commander, another_role).predicate(ctx)
      await remove(self)

      return await ctx.channel.send(f"The bot has been disabled.{self.asher}")

    except discord.ext.commands.errors.MissingAnyRole:
      await ctx.send('You do not have permissions to use that command')
      return

async def remove(self):
  for file in os.listdir("cogs"):
    if file.endswith(".py"):
      file = f"cogs.{file[:-3]}"
      self.client.unload_extension(file)


class reload(Cog):
  def __init__(self, client):
    self.client = client

  @command()
  async def reload(self, ctx):
    try:
      await has_any_role(bot_commander, another_role).predicate(ctx)
      await reloading(self)
      return await ctx.channel.send(f"All of the cogs have been reloaded.")
    except discord.ext.commands.errors.MissingAnyRole:
      await ctx.send('You do not have permissions to use that command')
      return

      
async def reloading(self):
  for file in os.listdir("cogs"):
    if file.endswith(".py"):
      file = f"cogs.{file[:-3]}"
      self.client.reload_extension(file)
  


def setup(client):
  client.add_cog(reload(client))
  client.add_cog(disabling_reenableing_cogs(client))
