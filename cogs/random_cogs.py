from discord.ext.commands import Cog, command
import discord
import random

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

def setup(client):
  client.add_cog(random_cogs(client))