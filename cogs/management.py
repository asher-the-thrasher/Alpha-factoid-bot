import discord
from discord.ext.commands import Cog,command,has_any_role
from discord.ext import tasks
from editable.config import Config  
another_role=Config.another_role
bot_commander=Config.bot_commander
import os


class Shutdown(Cog):
  def __init__(self, client):
    self.client = client

  @command()
  async def shutdown(self, ctx):
  
    members = (await self.client.application_info()).team.members
    if ctx.author in members:
      await remove(self)


      return await ctx.channel.send(f"The bot has been disabled.")

    else:
      await ctx.send('You do not have permissions to use that command')
      return

  @command()
  async def load(self, ctx):
    members = (await self.client.application_info()).team.members
    if ctx.author in members:

      await loading(self)
      await Reload.reloading_bot.start(self)
      
      return await ctx.channel.send(f"All of the cogs have been loaded.")
    else:
      await ctx.send('You do not have permissions to use that command')
      return


async def remove(self):
  management = 'management.py'
  for file in os.listdir("cogs"):
    if file.endswith(".py"):
      if file not in management:
        file = f"cogs.{file[:-3]}"
        self.client.unload_extension(file)


class Reload(Cog):
  def __init__(self, client):
    self.client = client

  @command(alias='update')
  async def reload(self, ctx):
    members = (await self.client.application_info()).team.members
    if ctx.author in members:
      #await has_any_role(bot_commander, another_role).predicate(ctx)
      await reloading(self)
      
      return await ctx.channel.send(f"All of the cogs have been reloaded.")
    else:
      await ctx.send('You do not have permissions to use that command')
      return





  @Cog.listener()
  async def on_ready(self):
    await Reload.reloading_bot.start(self)



  @tasks.loop(seconds=60)
  async def reloading_bot(self):
    await reloading(self)
      
async def reloading(self):
  
  for file in os.listdir("cogs"):
    if file.endswith(".py"):

        file = f"cogs.{file[:-3]}"
        self.client.reload_extension(file)
  self.client.reload_extension(f"editable.config")
  from editable.config import Config
  command_prefix = Config.command_prefix

  self.client.command_prefix = command_prefix


async def loading(self):
  management = 'management.py'

  for file in os.listdir("cogs"):
    if file.endswith(".py"):
      if file not in management:
        file = f"cogs.{file[:-3]}"
        self.client.load_extension(file)




def setup(client):
  client.add_cog(Reload(client))
  client.add_cog(Shutdown(client))
