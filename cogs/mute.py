import discord
from discord import Message
from discord.ext import commands, tasks
import asyncio
import datetime as dt
from datetime import datetime

from replit import db
from editable.config import Muted_role
from editable.config import guild_id

from discord.utils import get

from utils.bot_log import log_message
from editable.config import link_role_whitelist
from editable.config import bot_commander, another_role, alpha_mod

#base from https://www.codegrepper.com/code-examples/python/discord.py+mute
#Timed mute this format: 1d, 20s, 30m, etc..

async def create_mute(ctx, member: discord.Member=None, time=None, *, reason=None):
      try:
        time = time.lower()
        seconds = int(time[:-1]) #Gets the numbers from the time argument, start to -1
        duration = time[-1] #Gets the timed maniulation, s, m, h, d
        if duration == "s":
          seconds = seconds * 1
        elif duration == "m":
          seconds = seconds*60
        elif duration == "h":
          seconds = seconds * 60 * 60
        elif duration == "d":
          seconds = seconds * 86400
        else:
          await ctx.send("Invalid duration input")
          return
      except Exception:
          await ctx.send("Invalid time input")
          return

      unmute_time = (datetime.now() + dt.timedelta(seconds=seconds))
      member_id = member.id

      #muting
      muted = ctx.guild.get_role(Muted_role)

      await member.add_roles(muted, reason=reason)

      db[f"!?!?!?!? {member_id}"] = str(unmute_time)

class MuteCog(commands.cog.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['tempmute'])
  async def mute(self, ctx, member: discord.Member=None, time=None, *, reason=None):
      allowed_to_use = False
      for roles in link_role_whitelist:
          roles = get(ctx.guild.roles, id=roles)
          role = discord.utils.find(lambda r: r.name == str(roles), ctx.guild.roles)

          if role in ctx.author.roles:
              allowed_to_use = True
          if role in member.roles:
              await ctx.send("Really? Honestly, I'm embarrassed for you.")
              return

      if not allowed_to_use:
        return
      
      if not member:
        await ctx.send("You must mention a member to mute!")
        return
      elif not time:
        await ctx.send("You must mention a time to mute!")
        return
      else:
        if not reason:
          reason="No reason given"

      # Actually mutes
      await create_mute(ctx=ctx, member=member, time=time, reason=reason)
      
      #send message
      await ctx.message.delete()
      muted_embed = discord.Embed(title="", description=f"**{member} was muted **| {time} - {reason}", color = 0xFF0000)
      await ctx.send(embed=muted_embed)

      await log_message(self.bot, f"User Muted ({time})", f"**REASON:** {reason}", member, ctx.channel)
      
class UnMuteCog(commands.Cog):
  def __init__(self, client):
      self.client = client

  #manual unmute
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def unmute(self, ctx, member: discord.Member=None):
    if not member:
      await ctx.send("You must mention a member to unmute!")
      return
    
    muted = ctx.guild.get_role(Muted_role)
    await member.remove_roles(muted)
    await ctx.message.delete()

    muted_embed = discord.Embed(title="", description=f"**{member.mention} was unmuted.**")
    member_id = member.id
    del db[f"!?!?!?!? {str(member_id)}"]

    await ctx.send(embed=muted_embed)

    await log_message(self.client, "User Manually Unmuted", f"User {member.name} has been unmuted by {ctx.author}", member, color=0x00ff00)

    return


  @tasks.loop(seconds=10)
  async def doThisEveryTenSeconds(self, client):
    members_muted = db.prefix("!?!?!?!? ")

    if len(members_muted) > 0:
      for member in members_muted:
        unmute_time = db[member]
        value_time = str(unmute_time)
        current_time  = str(datetime.now())

        if value_time < current_time:
          guild = client.get_guild(guild_id)
          member_id = member[9:]
          user = guild.get_member(int(member_id))

          if user:  
            muted_id = guild.get_role(Muted_role)

            await user.remove_roles(muted_id, reason=None, atomic=True)
          
            await log_message(client, "User Unmuted (Auto)", f"User <@{member_id}> has been unmuted", user, color=0x00ff00)
          else:
            await log_message(client, "User Unmuted (Auto)", f"User <@{member_id}> has been unmuted", color=0x00ff00)

          del db[member]

          

  @commands.command()
  async def moderations(self, ctx):
    try:
        await commands.has_any_role(bot_commander, another_role, alpha_mod, 526611856237002753).predicate(ctx)

        members_muted = db.prefix("!?!?!?!? ")
        if len(members_muted) > 0:
          muted = []
          for member in members_muted:
            member_id = member[9:]

            # # this is really dumb
            # if time.day - datetime.now().day > 0:
            #   days_remaning = time.day - datetime.now().day
            # else:
            #   days_remaning = 0
            
            # if time.hour - datetime.now().hour > 0:
            #   hours_remaning = time.hour - datetime.now().hour
            # elif time.hour - datetime.now().hour < 0:
            #   hours_remaning = 24 + (time.hour - datetime.now().hour)
            # else:
            #   hours_remaning = 0

            # if time.minute - datetime.now().minute > 0:
            #   minutes_remaning = time.minute - datetime.now().minute
            # elif time.minute - datetime.now().minute < 0:
            #   minutes_remaning = 60 + time.minute - datetime.now().minute
            # else:
            #   minutes_remaning = 0

            # if time.second - datetime.now().second > 0:
            #   seconds_remaning = time.second - datetime.now().second
            # elif time.second - datetime.now().second < 0:
            #   seconds_remaning = 60 + time.second - datetime.now().second
            # else:
            #   seconds_remaning = 0
            # time_remaning = (f"{days_remaning} days, {hours_remaning} hours, {minutes_remaning} minutes, {seconds_remaning} seconds")
            # print(time_remaning)
            #print(member)
            
            user = ctx.guild.get_member(int(member_id))
            if user:
              db[member]
              #unmute_time = datetime.strptime(db[member], '%Y-%m-%d %H-%M-%S-%f')
              #current_time = datetime.strptime(datetime.now(), '%Y-%m-%d %H-%M-%S-%f')

              #print(unmute_time - datetime.now())

              muted.append(f"<@{str(user.id)}> - {db[member]}")
          
            
            
            # + " - Unmuted: " + time_remaning)
          embed_buider = discord.Embed(title="Muted Users", description='\n'.join(muted), color=0xFF0000)
          return await ctx.send(embed=embed_buider)
        ctx.send("No users muted")

    except discord.ext.commands.errors.MissingRole:
        return  

def setup(client):
  client.add_cog(UnMuteCog(client))
  client.add_cog(MuteCog(client))