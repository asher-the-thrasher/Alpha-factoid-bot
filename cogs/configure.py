import discord
from discord.ext import commands
from discord.utils import get
import asyncio
from discord_slash.utils import manage_components
from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow
from discord_slash.context import ComponentContext
import os

import json
from editable.config import Config 
admins=Config.admins
guild_id=Config.guild_id


async def reload(self):
  self.client.reload_extension(f"editable.config")

  for file in os.listdir("cogs"):
    if file.endswith(".py"):
      file = f"cogs.{file[:-3]}"
      self.client.reload_extension(file)


class ConfigurationUtilities(commands.Cog):
  def __init__(self, client):
    self.client = client



  async def changing_it(self, ctx, thing_to_change, changing,json_name):

    if not is_admin(ctx):
      await ctx.send("You can't use that command <:cheems:840763597508313109>")
      return
    
    if not thing_to_change:
      return await ctx.send(f"Please include a new {thing_to_change}.")

    emoji = '\N{THUMBS UP SIGN}'
    embed_builder = discord.Embed(title=f"Changing {thing_to_change}",description=f"To confirm you would like to change the {thing_to_change} to {changing} please react with {emoji}")
    embed_builder.set_footer(text="This will close out automatically in 30 sec.")
    message = await ctx.send(embed=embed_builder)
    await message.add_reaction(emoji)
    

    def check(reaction, user):
      result = (user == ctx.author) and str(reaction.emoji) == '👍' and reaction.message == message
      return result 
    
    confirmation = None
    try:
      reaction, user = await self.client.wait_for("reaction_add", timeout=30.0, check=check) 
      confirmation = True
    except asyncio.TimeoutError:
      embed_builder = discord.Embed(title=f"Changing {thing_to_change}",description=f"The reaction has timed out, please send the command again to change the {thing_to_change}.")
      await message.clear_reaction(emoji)
      return await message.edit(embed=embed_builder)
      
    if confirmation:
      with open("editable/config.json") as json_file:
        data = json.loads(json_file.read()) 
        data[json_name]=changing
        with open('editable/config.json', 'w') as outfile:
          json.dump(data, outfile, indent=2)
      embed_builder = discord.Embed(title=f"Changing {thing_to_change}",description=f"The {thing_to_change} has been changed to {changing}")
      await message.clear_reaction(emoji)
      await message.edit(embed=embed_builder)
      await reload(self)
  

  @commands.command()
  async def configprefix(self, ctx, prefix=None):
    changing=prefix
    thing_to_change = "Bot Prefix"
    json_name = "command_prefix"
    await ConfigurationUtilities.changing_it(self,ctx,thing_to_change = thing_to_change,changing=changing,json_name=json_name)
    self.client.command_prefix = prefix

  @commands.command()
  async def configbotactivity(self, ctx, bot_activity=None):
    changing=bot_activity
    thing_to_change = "Bot Activity"
    json_name = "bot_activity"
    await ConfigurationUtilities.changing_it(self,ctx,thing_to_change = thing_to_change,changing=changing,json_name=json_name)
    game = discord.Game(changing)
    await self.client.change_presence( activity=game)



  channel_ids = create_select(
      custom_id="channel_ids",
      options=[  # the options in your dropdown
          
          create_select_option("share your content", value="share_your_content"),
          create_select_option("senpaibot", value="senpaibot"),
          create_select_option("watch list", value="watch_list")

      ],
      placeholder="Channel to change ID",  # the placeholder text to show when no options have been chosen
      min_values=1,  # the minimum number of options a user must select
      max_values=1,  # the maximum number of options a user can select
  )


  @commands.command()
  async def configchannel(self, ctx, channel_id=None):
    check=False
    
    for channel in self.client.get_guild(guild_id).channels:
      if str(channel.id) == str(channel_id):
        check = True
        message="Choose what channel to change the Channel ID for"
        component_message = await ctx.send(message, components=[create_actionrow(ConfigurationUtilities.channel_ids)])
        button_ctx: ComponentContext = await manage_components.wait_for_component(self.client, messages=component_message)
        await component_message.delete()

        changing=int(channel_id)
        selected=str(button_ctx.selected_options).replace("_", " ").replace("['","").replace("']","")
        thing_to_change = f"{selected} channel ID"
        json_naming = selected=str(button_ctx.selected_options).replace("['","").replace("']","")
        json_name = json_naming
        await ConfigurationUtilities.changing_it(self,ctx,thing_to_change = thing_to_change,changing=changing,json_name=json_name)
    if check is False:
      await ctx.send(f"{channel_id} is not a valid channel id")




  role_ids = create_select(
      custom_id="role_ids",
      options=[  # the options in your dropdown
          
          create_select_option("muted role", value="muted_role"),
          create_select_option("modmod", value="modmod"),
          create_select_option("alpha mod", value="alpha_mod"),
          create_select_option("smart peepo", value="smart_peepo")

      ],
      placeholder="Role to change ID",  # the placeholder text to show when no options have been chosen
      min_values=1,  # the minimum number of options a user must select
      max_values=1,  # the maximum number of options a user can select
  )


  @commands.command()
  async def configrole(self, ctx, role_id=None):
    check=False
    #for role in ctx.guild.roles:
    for role in self.client.get_guild(guild_id).roles:

      if str(role.id) == str(role_id):
        check = True
        message="Choose what role to change the role ID for"
        component_message = await ctx.send(message, components=[create_actionrow(ConfigurationUtilities.role_ids)])
        button_ctx: ComponentContext = await manage_components.wait_for_component(self.client, messages=component_message)
        await component_message.delete()

        changing=int(role_id)
        selected=str(button_ctx.selected_options).replace("_", " ").replace("['","").replace("']","")
        thing_to_change = f"{selected} role ID"
        json_naming = selected=str(button_ctx.selected_options).replace("['","").replace("']","")
        json_name = json_naming
        await ConfigurationUtilities.changing_it(self,ctx,thing_to_change = thing_to_change,changing=changing,json_name=json_name)
    if check is False:
      await ctx.send(f"{role_id} is not a valid role ID")


def is_admin(ctx):
  allowed = False
  for roles in admins:
    roles = get(ctx.guild.roles, id=roles)
    role = discord.utils.find(lambda r: r.name == str(roles), ctx.guild.roles)
    
    if role in ctx.author.roles:
      allowed = True
        
  if allowed:
    return True
  else:
    return False


      
def setup(client):
    client.add_cog(ConfigurationUtilities(client))

