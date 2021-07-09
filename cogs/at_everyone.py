from discord.ext.commands import Cog
from editable.config import link_role_whitelist
from discord.utils import get
import discord


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

    if "@everyone" in message.content.split():
        mention = message.author.mention

        await message.delete()
        
        return await message.channel.send(f"Hey {mention}, looks like you've tried to ping everyone. This is your only warning, if you do it again, you will be removed from the server :)")

    if "@here" in message.content.split():
        mention = message.author.mention

        await message.delete()
        
        return await message.channel.send(f"Hey {mention}, looks like you've tried to ping 'here'. This is your only warning, if you do it again, you will be removed from the server :)")

def setup(client):
    client.add_cog(at_everyone(client))