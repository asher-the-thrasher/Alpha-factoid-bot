from discord.ext.commands import Cog, command
import discord
from discord_slash import  model,context, cog_ext
from editable.config import link_role_whitelist
from discord.utils import get


class UserInfo(Cog):
  def __init__(self, client):
    self.client = client
    



  @cog_ext.cog_context_menu(target=model.ContextMenuType.USER,name="userinfo",guild_ids=[849649811241173072,473253164884295699])
            
  async def user_info(self, ctx: context.MenuContext):
    allowed_to_use = False
    for roles in link_role_whitelist:
      roles = get(ctx.guild.roles, id=roles)
      role = discord.utils.find(lambda r: r.name == str(roles), ctx.guild.roles)

      if role in ctx.author.roles:
        allowed_to_use = True
        
    if not allowed_to_use:
      await ctx.send('You do not have permissions to use that command',hidden = True)
      return

        
    user=ctx.target_author
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=0xdfa3ff, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))

    embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)

    embed.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=embed, hidden = True)


  @command()
  async def userinfo(self,ctx, *, user: discord.Member = None): 
    allowed_to_use = False
    for roles in link_role_whitelist:
      roles = get(ctx.guild.roles, id=roles)
      role = discord.utils.find(lambda r: r.name == str(roles), ctx.guild.roles)

      if role in ctx.author.roles:
        allowed_to_use = True
        
    if not allowed_to_use:
      await ctx.send('You do not have permissions to use that command')
      return
    if user is None:
        user = ctx.author     
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=0xdfa3ff, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)

    embed.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=embed)
        
    

def setup(client):
  client.add_cog(UserInfo(client))