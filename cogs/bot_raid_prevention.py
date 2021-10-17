
import asyncio
import json

import discord
from discord.ext.commands import command, Cog
from discord.utils import get
from datetime import datetime

from editable.config import configure
log_channel=configure.log_channel
admins=configure.admins
guild_id=configure.guild_id
modmod=configure.modmod
from discord.ext.tasks import loop
from utils.bot_log import log_message


class RaidProt(Cog):
    def __init__(self, client):
        self.client = client

    async def writing_to_users_joined(users_joined=None, mods_warned=None, users_banned=None, banlock=None):
        with open("editable/users_joined.json", "r") as json_file:
            data = json.loads(json_file.read())

            if users_joined is None:
              data['users_joined'] = data['users_joined']
            else:
              data['users_joined'] = users_joined

            if mods_warned is None:
              data['mods_warned'] = data['mods_warned']
            else:
              data['mods_warned'] = mods_warned

            if users_banned is None:
              data['users_banned'] = data['users_banned']
            else:
              data["users_banned"] = users_banned

            if banlock is None:
              data['banlock'] = data['banlock']
            else:
              data['banlock'] = banlock

            with open('editable/users_joined.json', 'w') as outfile:
                json.dump(data, outfile, indent=2)

    async def reading_from_users_joined(users_joined=False, mods_warned=False, users_banned=False, banlock=False):
        with open("editable/users_joined.json", "r") as json_file:
            data = json.loads(json_file.read())

            if users_joined is True:
                return int(data['users_joined'])

            if mods_warned is True:
                if int(data['mods_warned']) ==0:
                  return False
                if int(data['mods_warned']) ==1:
                  return True

            if users_banned is True:
                return int(data['users_banned'])

            if banlock is True:
                if int(data['banlock']) ==0:
                  return False
                if int(data['banlock']) ==1:
                  return True

    @loop(seconds=60)
    async def user_join_reset(self):
        banlock = await RaidProt.reading_from_users_joined(banlock=True)
        mods_warned = await RaidProt.reading_from_users_joined(mods_warned=True)

        if banlock is False and mods_warned is False:
            await RaidProt.writing_to_users_joined(users_joined=0)


    """@command()
    async def joined(self, ctx):
        file_content = await RaidProt.reading_from_users_joined(users_joined=True)
        users_joined = file_content + 3
        await RaidProt.writing_to_users_joined(users_joined=users_joined)"""

    @Cog.listener()
    async def on_member_join(self, member):
        if member.avatar_url == member.default_avatar_url:
            users_joined = await RaidProt.reading_from_users_joined(users_joined=True)
            users_joined = users_joined + 1
            await RaidProt.writing_to_users_joined(users_joined=users_joined)
        lock = await RaidProt.reading_from_users_joined(banlock=True)
        users_joined = await RaidProt.reading_from_users_joined(users_joined=True)
        mods_warned = await RaidProt.reading_from_users_joined(mods_warned=True)

        if (users_joined == 4 and not lock) or (not mods_warned and users_joined >= 5):
            await RaidProt.writing_to_users_joined(mods_warned=1)
            emoji = '\N{THUMBS UP SIGN}'
            embed_builder = discord.Embed(title=f"Potential Bot Raid ({users_joined} Users)",
            description=f"An unusually high number of users with default profile pictures have joined the server in a 1 minute window, if you would like to turn on Ban Lock use ?banlock. If you believe this warning warning is a false positive, react with {emoji} so you get warned the next time there is a suspected raid.",
            color=0xf5c242)
            embed_builder.timestamp = datetime.now()
            
            self.warning_raid = await self.client.get_channel(log_channel).send(f"<@&{modmod}>", embed=embed_builder)
            await self.warning_raid.add_reaction(emoji)

            def check(reaction, user):

                if user is not self.client.user:
                    for role in user.roles:
                        for admin in admins:

                            guild = self.client.get_guild(guild_id)
                            admin_role = get(guild.roles, id=admin)
                            result = role == admin_role and str(
                                reaction.emoji) == '👍' and reaction.message == self.warning_raid
                            if result is True:
                                return result

            result = await self.client.wait_for("reaction_add", check=check)
            result = True

            if result is True:
                users_joined = await RaidProt.reading_from_users_joined(users_joined=True)

                await RaidProt.writing_to_users_joined(mods_warned=0, users_joined=0)
                embed_builder = discord.Embed(title=f"Potential Bot Raid ({users_joined} Users)",
                description="A Mod has marked the bot raid warning system as a false positive.")
                
                await self.warning_raid.edit(embed=embed_builder)

        if users_joined >= 5 and not lock and mods_warned:
            emoji = '\N{THUMBS UP SIGN}'

            embed_builder = discord.Embed(title=f"Potential Bot Raid ({users_joined} Users)",
            description=f"An unusually high number of users with default profile pictures have joined the server in a 1 minute window, if you would like to turn on Ban Lock use ?banlock. If you believe this warning warning is a false positive, react with {emoji} so you get warned the next time there is a suspected raid.",
            color=0xf5c242)

            await self.warning_raid.edit(content=f"<@&{modmod}>", embed=embed_builder)

        if lock:
            if member.avatar_url == member.default_avatar_url:
                users_banned = await RaidProt.reading_from_users_joined(users_banned=True)
                users_banned += 1
                await RaidProt.writing_to_users_joined(users_banned=users_banned)

                if users_banned == 1:
                    embed_builder = discord.Embed(title="Ban Lock On", description=f"Users Banned: {users_banned}")
                    embed_builder.timestamp = datetime.now()

                    users_banned_message = await self.client.get_channel(log_channel).send(embed=embed_builder)
                    self.users_banned_message = users_banned_message

                embed_builder = discord.Embed(
                    description="Hi! You have been banned from the Alpha Gaming discord server. We are currently experiencing a bot raid and are banning anyone who joins right now. If you are not a bot and this was a mistake please fill out our unban form https://forms.gle/6C3u5URiMUXvxgEu7 and we will unban you as soon as we can.")
                try:
                    dm = await member.create_dm()
                    await dm.send(embed=embed_builder)
                    await member.ban(reason="Bot raid, ban lock was turned on")
                    embed_builder = discord.Embed(title="Ban Lock On", description=f"Users Banned: {users_banned}")
                    await self.users_banned_message.edit(embed=embed_builder)
                except:
                    await member.ban(reason="Bot raid, ban lock was turned on, dms off")
                    embed_builder = discord.Embed(title="Ban Lock On", description=f"Users Banned: {users_banned}")
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
        lock = await RaidProt.reading_from_users_joined(banlock=True)
        if lock:
            return await ctx.send('The ban lock is currently on, if you would like to turn it off use ?banunlock')

        emoji = '\N{THUMBS UP SIGN}'
        embed_builder = discord.Embed(title=f"Raid protection banning system",
        description=f"To confirm you would like to turn on ban lock react with {emoji}")
        
        embed_builder.set_footer(text="This will close out automatically in 30 sec.")
        
        message = await ctx.send(embed=embed_builder)
        await message.add_reaction(emoji)

        def check(reaction, user):
            for role in user.roles:
                for admin in admins:
                    admin_role = get(ctx.guild.roles, id=admin)
                    result = role == admin_role and str(reaction.emoji) == '👍' and reaction.message == message
                    if result is True:
                        return result

        confirmation = None
        try:

            reaction, user = await self.client.wait_for("reaction_add", timeout=30.0, check=check)
            confirmation = True

        except asyncio.TimeoutError:
            embed_builder = discord.Embed(title=f"Raid protection banning system",
            description=f"The raid protection system has timed out, please send ?banlock again to turn the system on.")
            
            await message.clear_reaction(emoji)
            
            return await message.edit(embed=embed_builder)

        if confirmation:
            await RaidProt.writing_to_users_joined(banlock=1)
            embed_builder = discord.Embed(title=f"Raid protection banning system",
            description=f"The raid protection system has been activated and will ban all new members with a default profile picture. To turn off the raid protection system, send ?banunlock")
            
            await message.edit(embed=embed_builder)
            await log_message(self.client, title=f"Raid protection banning system", body=f"The raid protection system has been activated and will ban all new members with a default profile picture. To turn off the raid protection system, send ?banunlock", user=None, channel=None, moderator = ctx.author)
            

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
        lock = await RaidProt.reading_from_users_joined(banlock=True)
        if not lock:
            return await ctx.send('The ban lock is not currently on, if you would like to turn it on use ?banlock')

        emoji = '\N{THUMBS UP SIGN}'
        embed_builder = discord.Embed(title=f"Raid protection banning system",
        description=f"To confirm you would like to turn off ban lock react with {emoji}")

        embed_builder.set_footer(text="This will close out automatically in 30 sec.")

        message = await ctx.send(embed=embed_builder)
        await message.add_reaction(emoji)

        def check(reaction, user):
            for role in user.roles:
                for admin in admins:
                    admin_role = get(ctx.guild.roles, id=admin)
                    result = role == admin_role and str(reaction.emoji) == '👍' and reaction.message == message
                    if result is True:
                        return result

        confirmation = None
        try:
            reaction, user = await self.client.wait_for("reaction_add", timeout=30.0, check=check)
            confirmation = True
        except asyncio.TimeoutError:
            embed_builder = discord.Embed(title=f"Raid protection banning system",
            description=f"The raid protection system has timed out, please send ?banunlock again to turn the system off.")
            
            await message.clear_reaction(emoji)
            return await message.edit(embed=embed_builder)

        if confirmation:
            await RaidProt.writing_to_users_joined(banlock=0, users_banned=0, users_joined=0, mods_warned=0)

            embed_builder = discord.Embed(title=f"Raid protection banning system",
            description=f"The raid protection system has been turned off. To turn the system back on send ?banlock")
            
            await message.edit(embed=embed_builder)


def setup(client):
    client.add_cog(RaidProt(client))
