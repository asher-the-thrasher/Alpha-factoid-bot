from discord.ext.commands import command, Cog
import discord
from editable.config import log_channel, modmod, admins
import asyncio
from discord.utils import get

class RaidProt(Cog):
  def __init__(self, client):
    self.client = client
    self.lock = False
    self.users_joined = 0
    self.users_banned = 0

  @Cog.listener()
  async def on_member_join(self, member):
    if member.avatar_url == member.default_avatar_url:
      self.users_joined += 1
    
    if self.users_joined >= 4 and not self.lock:

      embed_builder = discord.Embed(title=f"Potential Bot Raid ({self.users_joined} Users)", description=f"An unusually high number of users with default profile pictures have joined the server in a 1 minute window, if you would like to turn on Ban Lock use ?banlock", color=0xf5c242)

      
      await self.client.get_channel(log_channel).send(f"<@{modmod}>", embed=embed_builder)
      
    if self.lock:
      if member.avatar_url == member.default_avatar_url:
        self.users_banned += 1
        if self.users_banned == 1:
          embed_builder = discord.Embed(title=f"Users Banned: {self.users_banned}") 
          users_banned_message = await self.client.get_channel(log_channel).send(embed=embed_builder)
          self.users_banned_message = users_banned_message
          
        dm = await member.create_dm() 
        await dm.send("Hi! You have been banned from the Alpha Gaming discord server. We are currently experiencing a bot raid and are banning anyone who joins right now. If you are not a bot and this was a mistake please fill out our unban form https://forms.gle/6C3u5URiMUXvxgEu7 and we will unban you as soon as we can.")
        await member.ban(reason="Bot raid, ban lock was turned on")
        embed_builder = discord.Embed(title=f"Users Banned: {self.users_banned}") 
        await self.users_banned_message.edit(embed=embed_builder)




  @command()
  async def banlock(self, ctx):
    allowed = False
    for roles in admins:
      roles = get(ctx.guild.roles, id=roles)
      role = discord.utils.find(lambda r: r.name == str(roles), ctx.guild.roles)
      
      if role in ctx.author.roles:
        allowed = True
      

    if not allowed:
      await ctx.send('You do not have permissions to use that command')
      return

    emoji = '\N{THUMBS UP SIGN}'
    embed_builder = discord.Embed(title=f"Raid protection banning system",description=f"To confirm you would like to turn on ban lock react with {emoji}")
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
      embed_builder = discord.Embed(title=f"Raid protection banning system",description=f"The raid protection system has timed out, please send ?banlock again to turn the system on.")
      await message.clear_reaction(emoji)
      return await message.edit(embed=embed_builder)
      
    if confirmation:
      self.lock = True
      embed_builder = discord.Embed(title=f"Raid protection banning system",description=f"The raid protection system has been activated and will ban all new members with a default profile picture. To turn off the raid protection system, send ?banunlock")
      await message.edit(embed=embed_builder)





  @command(name="banunlock")
  async def ban_unlock(self, ctx):
    allowed = False
    for roles in admins:
      roles = get(ctx.guild.roles, id=roles)
      role = discord.utils.find(lambda r: r.name == str(roles), ctx.guild.roles)
      
      if role in ctx.author.roles:
        allowed = True

    if not allowed:
      await ctx.send('You do not have permissions to use that command')

      return

    emoji = '\N{THUMBS UP SIGN}'
    embed_builder = discord.Embed(title=f"Raid protection banning system",description=f"To confirm you would like to turn off ban lock react with {emoji}")
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
      embed_builder = discord.Embed(title=f"Raid protection banning system",description=f"The raid protection system has timed out, please send ?banunlock again to turn the system off.")
      await message.clear_reaction(emoji)
      return await message.edit(embed=embed_builder)
      
    if confirmation:
      self.lock = False
      embed_builder = discord.Embed(title=f"Raid protection banning system",description=f"The raid protection system has been turned off. To turn the system back on send ?banlock")
      await message.edit(embed=embed_builder)


  @discord.ext.tasks.loop(seconds=60)
  async def user_join_reset(self):
    self.users_joined = 0


def setup(client):
  print("ig i have to do this")
  """client.add_cog(RaidProt(client))"""
