import discord
from editable.config import configure
log_channel=configure.log_channel

async def log_message(bot, title, body, user=None, channel=None, color=0xFF0000):
  embed_buider = discord.Embed(title=title, description=body, color=color)
  if channel:
    embed_buider.add_field(name="channel", value=f"<#{channel.id}>", inline=False)

  if user:
    embed_buider.set_footer(text=f"  User: {str(user)}\nID: {str(user.id)}",  icon_url = user.avatar_url)
                
  await bot.get_channel(log_channel).send(embed=embed_buider)