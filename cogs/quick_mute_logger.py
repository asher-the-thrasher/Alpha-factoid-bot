from discord.ext.commands import Cog
from discord_slash import  model,context, cog_ext
from editable.config import Config
watch_list=Config.watch_list
guild_ids=Config.guild_ids
link_role_whitelist=Config.link_role_whitelist
from cogs.mute import create_mute
import discord
from discord.utils import get
from utils.bot_log import log_message



class ContextMenus(Cog):
  def __init__(self, bot):
    self.bot = bot

  @cog_ext.cog_context_menu(target=model.ContextMenuType.USER,name="mute",guild_ids=guild_ids)
            
  async def mute(self, ctx: context.MenuContext):
    allowed_to_use = False
    for roles in link_role_whitelist:
      roles = get(ctx.guild.roles, id=roles)
      role = discord.utils.find(lambda r: r.name == str(roles), ctx.guild.roles)

      if role in ctx.author.roles:
        allowed_to_use = True
      
      if role in ctx.target_author.roles:
        await ctx.send("Really? You just tried to quick mute a mod, smooth.", hidden = True)
        return
    if not allowed_to_use:
      await ctx.send('You do not have permissions to use that command',hidden = True)
      return
    
    member=ctx.target_author
    reason = "Breaking the rules, speed mute"
    time = "3d"
    await create_mute(ctx=ctx, member=ctx.target_author, time=time, reason=reason)
    muted_embed = discord.Embed(title="", description=f"**{member} was muted **| {time} - {reason}", color = 0xFF0000)
    await ctx.send(embed=muted_embed)

    await log_message(self.bot, f"User Muted ({time})", f"**REASON:** {reason}", member, ctx.channel,moderator=ctx.author)
    
  # Auto creates a log in #watch-list
  @cog_ext.cog_context_menu(target=model.ContextMenuType.MESSAGE,name="Auto-Log",guild_ids=guild_ids)
  async def log_message(self, ctx: context.MenuContext):
    allowed_to_use = False
    for roles in link_role_whitelist:
      roles = get(ctx.guild.roles, id=roles)
      role = discord.utils.find(lambda r: r.name == str(roles), ctx.guild.roles)

      if role in ctx.author.roles:
        allowed_to_use = True

    if not allowed_to_use:
      await ctx.send(content = 'You do not have permissions to use that command',hidden = True)
      return
    #embed_builder= discord.Embed(title=f"{ctx.target_message.author}\n{ctx.target_message.author.id}", description=f"{ctx.target_message.content}", color=0x00ff00, set_author=ctx.author)

    title = "Message Logged"
    body = ctx.target_message.content
    user = ctx.target_message.author
    channel = ctx.target_message.channel
    color=0x00ff00
    embed_buider = discord.Embed(title=title, description=body, color=color)
    if channel:
      embed_buider.add_field(name="channel", value=f"<#{channel.id}>", inline=False)

    if user:
      embed_buider.set_footer(text=f"  User: {str(user)}\nID: {str(user.id)}",  icon_url = user.avatar_url)

    await self.bot.get_channel(watch_list).send(embed=embed_buider)
    

    await ctx.send(content=f"Logged message from user <@{ctx.target_message.author.id}>",hidden=True)
    


def setup(bot):
  bot.add_cog(ContextMenus(bot))