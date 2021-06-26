import datetime as dt

import discord
from discord.ext import commands, tasks
from replit import db
from editable.config import Muted_role
from editable.config import guild_id


# base from https://www.codegrepper.com/code-examples/python/discord.py+mute
# Timed mute this format: 1d, 20s, 30m, etc..
class MuteCog(commands.cog.Cog):
    @commands.command(aliases=['tempmute'])
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member = None, time=None, *, reason=None):
        if not member:
            await ctx.send("You must mention a member to mute!")
            return
        elif not time:
            await ctx.send("You must mention a time to mute!")
            return
        else:
            if not reason:
                reason = "No reason given"
        # Now timed mute manipulation
        try:
            seconds = int(time[:-1])  # Gets the numbers from the time argument, start to -1
            duration = time[-1]  # Gets the timed maniulation, s, m, h, d
            if duration == "s":
                seconds = seconds * 1
            elif duration == "m":
                seconds = seconds * 60
            elif duration == "h":
                seconds = seconds * 60 * 60
            elif duration == "d":
                seconds = seconds * 86400
            else:
                await ctx.send("Invalid duration input")
                return
        except Exception as e:
            await ctx.send("Invalid time input")
            return

        unmute_time = (dt.datetime.now() + dt.timedelta(seconds=seconds))

        guild = ctx.guild

        # muting

        Muted = discord.utils.get(guild.roles, name=Muted_role)
        await member.add_roles(Muted, reason=reason)
        await ctx.message.delete()
        muted_embed = discord.Embed(title="", description=f"**{member.mention} was muted **| {time} - {reason}")
        member_id = member.id
        await ctx.send(embed=muted_embed)
        db[f"!?!?!?!? {member_id}"] = str(unmute_time)
        print(f"!?!?!?!? {member_id}")


class UnMuteCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    # manual unmute
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send("You must mention a member to unmute!")
            return

        guild = ctx.guild
        Muted = discord.utils.get(guild.roles, name=Muted_role)
        await member.remove_roles(Muted)
        muted_embed = discord.Embed(title="", description=f"*{member.mention} was unmuted.*")
        member_id = member.id
        del db[str(member_id)]

        await ctx.send(embed=muted_embed)
        return

    @tasks.loop(seconds=10)
    async def doThisEveryTenSeconds(self, client):
        members_muted = db.prefix("!?!?!?!? ")
        print(members_muted)
        if len(members_muted) > 0:
            for member in members_muted:
                value = db[member]
                value_time = str(value)
                current_time = str(dt.datetime.now())
                if value_time < current_time:
                    guild = client.get_guild(guild_id)
                    print(member)
                    # member = member[9:].split()
                    print(str(member))
                    member = member[0:].lower()
                    print("this")
                    print(member)
                    member = guild.get_member(int(member))
                    Muted = discord.utils.get(guild.roles, name=Muted_role)
                    await member.remove_roles(Muted, reason=None, atomic=True)
                    del db[str(member.id)]
        else:
            print("oh no")


def setup(client):
    client.add_cog(UnMuteCog(client))
    client.add_cog(MuteCog(client))
