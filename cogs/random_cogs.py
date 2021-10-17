from discord.ext.commands import Cog, command
import discord
import random
from editable.config import configure
link_role_whitelist=configure.link_role_whitelist
admins = configure.admins
from discord.utils import get



potato_images = [
  "https://i5.walmartimages.ca/images/Large/094/507/6000200094507.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Russet_potato_cultivar_with_sprouts.jpg/1920px-Russet_potato_cultivar_with_sprouts.jpg",
  "https://api.time.com/wp-content/uploads/2020/04/Boss-Turns-Into-Potato.jpg",
  "https://t3.ftcdn.net/jpg/00/85/79/92/360_F_85799278_0BBGV9OAdQDTLnKwAPBCcg1J7QtiieJY.jpg",
  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcf4lvLnDjUNKkVBWKAfLb6X5QXS_VB1ZQag&usqp=CAU"
]

class random_cogs(Cog):
  def __init__(self, bot):
    self.bot = bot

  @command()
  async def potato(self, ctx):
    embed = discord.Embed()
    embed.set_image(url=random.choice(potato_images))

    return await ctx.channel.send(embed=embed)

  @command()
  async def ping(self, ctx):
    ping = int(self.bot.latency * 1000)
    return await ctx.channel.send(f"It has been {ping} ms")



  @command()
  async def send(self, ctx,channel_send: discord.TextChannel = None,*,message):
    if not is_admin(ctx):
      return
    if not channel_send:
      return await ctx.send("No channel specified")
    await self.bot.get_channel(channel_send.id).send(message)
    emoji = '\N{THUMBS UP SIGN}'
    await ctx.message.add_reaction(emoji)
    
    
  @command()
  async def embed(self, ctx,channel_send: discord.TextChannel = None,*,title):
    if not admin(ctx):
      return
    if not channel_send:
      return await ctx.send("No channel specified")
    await ctx.send("What message would you like to send?")
    def check(m):
      if m.author == ctx.author and m.channel == ctx.channel:
        return m

    msg = await self.bot.wait_for('message', check=check)
    embed_builder = discord.Embed(title = title, description = msg.content, color = 0x3498db)
    await self.bot.get_channel(channel_send.id).send(embed=embed_builder)
    
    emoji = '\N{THUMBS UP SIGN}'
    await msg.add_reaction(emoji)

def is_admin(ctx):
  allowed = False
  for roles in link_role_whitelist:
    roles = get(ctx.guild.roles, id=roles)
    role = discord.utils.find(lambda r: r.name == str(roles), ctx.guild.roles)
    
    if role in ctx.author.roles:
      allowed = True
        
  if allowed:
    return True
  else:
    return False    

def admin(ctx):
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
  client.add_cog(random_cogs(client))