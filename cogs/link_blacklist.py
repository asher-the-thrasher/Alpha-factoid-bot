import json

import discord
from discord.ext import commands
from discord.ext.commands import Cog, command
from discord.utils import get

from editable.config import link_role_whitelist, bot_commander, another_role

from cogs.mute import MuteCog

class LinkBlacklist(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.channel.id != 857728639613272094:
            return

        # Checks if user is allowed to post links
        for roles in link_role_whitelist:
            roles = get(message.guild.roles, id=roles)
            role = discord.utils.find(lambda r: r.name == str(roles), message.guild.roles)

            if role in message.author.roles:
                return

        with open('editable/blacklisted_links.json') as json_file:
            blacklisted = json.load(json_file)

        # Loops through all disallowed links
        for b_link in blacklisted:
            if b_link in message.content:
                with open('editable/whitelisted_links.json') as json_file:
                    whitelisted = json.load(json_file)

                # Checks if the link is actually allowed
                for w_link in whitelisted:
                    if w_link in message.content:
                        print("okay link")
                        pass

                await message.delete()

                embed_buider = discord.Embed(title="Message Delted (Banned Link)", description=message.content, color=0xFF0000)
                embed_buider.add_field(name="User: " + str(message.author), value="ID: " + str(message.author.id), inline=False)

                await MuteCog.mute(MuteCog, message, message.author, "30s", "Self promotion")
                await message.channel.send("message deleted")
                await self.bot.get_channel(851970921501687828).send(embed=embed_buider)

    @command()
    async def addbl(self, ctx, link: str.lower = None):
        try:
            await commands.has_any_role(bot_commander, another_role).predicate(ctx)

            if not link:
                return await ctx.send("You need to add a link after `!addbl` to add it to the blacklist")

            with open('editable/blacklisted_links.json') as json_file:
                data = json.load(json_file)

            if link in data:
                return await ctx.send('That link is already blacklisted!')

            data[link] = []
            data[link].append(link)
            writing_to_json(data, "editable/blacklisted_links.json")

            return await ctx.channel.send("Added link blacklist")
        except discord.ext.commands.errors.MissingRole:
            return

    @command()
    async def addwl(self, ctx, link: str.lower = None):
        try:
            await commands.has_any_role(bot_commander, another_role).predicate(ctx)

            if not link:
                return await ctx.send("You need to add a link after `!addwl` to add it to the whitelist")

            with open('editable/whitelisted_links.json') as json_file:
                data = json.load(json_file)

            if link in data:
                return await ctx.send('That link is already whitelisted!')

            data[link] = []
            data[link].append(link)
            writing_to_json(data, "editable/whitelisted_links.json")

            return await ctx.channel.send("Added link whitelist")
        except discord.ext.commands.errors.MissingRole:
            return

    @command()
    async def delbl(self, ctx, link: str.lower = None):
        try:
            await commands.has_any_role(bot_commander, another_role).predicate(ctx)

            if not link:
                return await ctx.send("You need to add a link after `!delbl` to remove it from the blacklist")

            with open('editable/blacklisted_links.json') as data_file:
                data = json.load(data_file)
            data.pop(link)
            writing_to_json(data, 'editable/blacklisted_links.json')

            return await ctx.send("Link removed from blacklist")
        except discord.ext.commands.errors.MissingRole:
            return

    @command()
    async def delwl(self, ctx, link: str.lower = None):
        try:
            await commands.has_any_role(bot_commander, another_role).predicate(ctx)

            if not link:
                return await ctx.send("You need to add a link after `!delwl` to remove it from the whitelist")

            with open('editable/whitelisted_links.json') as data_file:
                data = json.load(data_file)
            data.pop(link)
            writing_to_json(data, 'editable/whitelisted_links.json')

            return await ctx.send("Link removed from whitelist")
        except discord.ext.commands.errors.MissingRole:
            return


def writing_to_json(data, file):
    with open(file, 'w') as outfile:
        json.dump(data, outfile, indent=2)


def setup(client):
    client.add_cog(LinkBlacklist(client))
