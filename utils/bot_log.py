import discord
from editable.config import configure
log_channel=configure.log_channel
from datetime import datetime

async def log_message(bot, title, body, user=None, channel=None, moderator = None,color=0xFF0000):
  embed_buider = discord.Embed(title=title, description=body, color=color)
  if channel:
    embed_buider.add_field(name="channel", value=f"<#{channel.id}>", inline=False)
  if moderator:
    embed_buider.add_field(name="Moderator", value=f"<#{moderator}>", inline=False)    
  if user:
    embed_buider.set_footer(text=f"  User: {str(user)}\nID: {str(user.id)}",  icon_url = user.avatar_url)
  embed_buider.timestamp = datetime.now()

  await bot.get_channel(log_channel).send(embed=embed_buider)