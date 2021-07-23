from discord.ext.commands import Cog
from editable.config import link_role_whitelist
from discord.utils import get
import discord
import json

from editable.config import log_channel
from cogs.mute import create_mute

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

    # Checks if user is allowed to post links
    for roles in link_role_whitelist:
        roles = get(message.guild.roles, id=roles)
        role = discord.utils.find(lambda r: r.name == str(roles), message.guild.roles)

        if role in message.author.roles:
            return

    if "@everyone" in message.content:
        await message.delete()

        with open("editable/bad_users.json") as json_file:
          data = json.load(json_file)

        if str(message.author.id) in data["users"].__str__():
          await deal_with_infractions(message, self.bot)

        else:
          await message.channel.send(f"Hey {message.author.mention}, looks like you've tried to ping everyone. This is your only warning, if you do it again, you will be removed from the server :)")

          data["users"].append({
            "author": message.author.id,
            "infractions": 1
          })

          writing_to_json(data)

    if "@here" in message.content.split():
        await message.delete()

        with open("editable/bad_users.json") as json_file:
          data = json.load(json_file)

        if str(message.author.id) in data["users"].__str__():
          await deal_with_infractions(message, self.bot)

        else:
          await message.channel.send(f"Hey {message.author.mention}, looks like you've tried to ping 'here'. This is your only warning, if you do it again, you will be removed from the server :)")

          data["users"].append({
            "author": message.author.id,
            "infractions": 1
          })

          writing_to_json(data)

def setup(client):
    client.add_cog(at_everyone(client))

async def deal_with_infractions(ctx, bot):
    with open("editable/bad_users.json") as json_file:
      data = json.load(json_file)

    for user in data["users"]:
      if ctx.author.id == user["author"]:
        user["infractions"] = user["infractions"] + 1

        writing_to_json(data)

        embed_buider = discord.Embed(title="Mass Ping ({infractions} infractions)".format(**user), description=ctx.content, color=0xFF0000)
        embed_buider.add_field(name="channel", value="<#" + str(ctx.channel.id) + ">", inline=False)
        embed_buider.set_footer(text=f"  User: {str(ctx.author)}\nID: {str(ctx.author.id)}",  icon_url = ctx.author.avatar_url)
                
        await bot.get_channel(log_channel).send(embed=embed_buider)

        if user["infractions"] == 2:
          await create_mute(ctx=ctx, member=ctx.author, time="3d", reason="Mass Ping")

          return await ctx.channel.send(f"Sadly, {ctx.author.mention} tried to mass ping everyone after being warned. They have now been muted.")

        if user["infractions"] >= 3:
          await ctx.author.kick(reason="@.everyone 3+ times")