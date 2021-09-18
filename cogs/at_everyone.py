from discord.ext.commands import Cog
from editable.config import configure
link_role_whitelist = configure.link_role_whitelist
from discord.utils import get
import discord
import json

from utils.bot_log import log_message
from cogs.mute import create_mute

mass_pings = ["@everyone", "@here"]
bad_mentions = [179980876027789312]

def writing_to_json(data):
    with open('editable/bad_users.json', 'w') as outfile:
      json.dump(data, outfile, indent=2)

class at_everyone(Cog):
  def __init__(self, bot):
    self.bot = bot

  @Cog.listener()
  async def on_message(self, message):
    if message.author.bot:
          return

    delete_message = False

    # Checks if user is allowed to post links
    for roles in link_role_whitelist:
        roles = get(message.guild.roles, id=roles)
        role = discord.utils.find(lambda r: r.name == str(roles), message.guild.roles)

        if role in message.author.roles:
            return

    for word in mass_pings:
      if word in message.content.lower():
        delete_message = True

        with open("editable/bad_users.json") as json_file:
          data = json.load(json_file)

        if str(message.author.id) in data["users"].__str__():
          await deal_with_infractions(message, self.bot)

        else:
          await message.channel.send(f"Hey {message.author.mention}, looks like you've tried to ping `{word}`. This is your only warning, if you do it again, you will be removed from the server. <:cheems:840763597508313109> ")

          data["users"].append({
            "author": message.author.id,
            "infractions": 1
          })

          writing_to_json(data)

    if message.mentions:
      for user in bad_mentions:
        mentioned = self.bot.get_user(user)
        if mentioned in message.mentions:
          delete_message = True

          with open("editable/bad_users.json") as json_file:
            data = json.load(json_file)

          if str(message.author.id) in data["users"].__str__():
            await deal_with_infractions(message, self.bot)

          else:
            await message.channel.send(f"Hello {message.author.mention}, looks like you've tried to ping {mentioned.name}. They have kindly requested not to be pinged, thank you! Unfortunately, if you do it again, you will be removed from the server. Kapeesh? <:cheems:840763597508313109> ")

            data["users"].append({
              "author": message.author.id,
              "infractions": 1
            })

            writing_to_json(data)

    if delete_message:
      await message.delete()

def setup(client):
    client.add_cog(at_everyone(client))

async def deal_with_infractions(ctx, bot):
    with open("editable/bad_users.json") as json_file:
      data = json.load(json_file)

    for user in data["users"]:
      if ctx.author.id == user["author"]:
        user["infractions"] = user["infractions"] + 1

        writing_to_json(data)

        await log_message(bot, 
        "Mass Ping ({infractions} infractions)".format(**user),
        ctx.content, ctx.author, ctx.channel)
                
        if user["infractions"] == 2:
          await create_mute(ctx=ctx, member=ctx.author, time="3d", reason="Mass Ping")

          return await ctx.channel.send(f"Sadly, {ctx.author.mention} tried to break the rules after being warned. They have now been muted.")
        
        if user["infractions"] >= 3:
          await ctx.author.kick(reason="@.everyone 3+ times")