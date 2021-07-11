import json

import discord
from discord.ext import commands
from discord.ext.commands import Cog, command
from discord.utils import get

from editable.config import link_role_whitelist, bot_commander, another_role, alpha_mod, share_content

from cogs.mute import create_mute

class LinkBlacklist(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
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
                        pass

                # allows certain links to be allowed in a certain channel
                if (message.channel.id == share_content) and (blacklisted.get(b_link)[0].get("sharable") == "yes"):
                  pass

                # Establishes a reason for the common ones
                if b_link == "https://twitch.tv/" or b_link == "https://www.twitch.tv/":
                  reason_muted = "twitch"
                elif b_link == "https://discord.gg/":
                  reason_muted = "discord"
                else:
                  reason_muted = "blacklisted"

                # Creates an embed message to go in bot logs
                embed_buider = discord.Embed(title="Message Deleted (Blacklisted Link)", description=message.content, color=0xFF0000)
                embed_buider.add_field(name="channel", value="<#" + str(message.channel.id) + ">", inline=False)
                embed_buider.set_footer(text=f"  User: {str(message.author)}\nID: {str(message.author.id)}",  icon_url = message.author.avatar_url)

                # To bot log channel
                await self.bot.get_channel(849649811241173075).send(embed=embed_buider)

                await message.delete()

                # replaces their message with an embed
                muted_embed = discord.Embed(title="", description=f"{message.author} just posted a {reason_muted} link and has been sent to naughty corner to think about what they did.", color = 0xFF0000)

                # to channel where blacklisted link was sent
                await message.channel.send(embed=muted_embed)

                # mutes
                await create_mute(ctx=message, member=message.author, time="1m", reason="Blacklisted Link")



    @command()
    async def addbl(self, ctx, link: str.lower = None, ping_mod="no"):
        try:
            await commands.has_any_role(bot_commander, another_role).predicate(ctx)

            if not (ping_mod == 'yes' or 'no'):
                return await ctx.send("You need to add if you want to ping a mod after the link in the form of 'yes' or 'no' to add it to the blacklist")

            if not link:
                return await ctx.send("You need to add a link after `!addbl` to add it to the blacklist")

            with open('editable/blacklisted_links.json') as json_file:
                data = json.load(json_file)

            if link in data:
                return await ctx.send('That link is already blacklisted!')

            data[link] = []
            data[link].append({
                'link': link,
                'ping mod': ping_mod
                })

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
            data[link].append({
              "link": link
            })
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

            if link not in data:
              return await ctx.send("That link is not blacklisted")

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

            if link not in data:
              return await ctx.send("That link is not whitelisted")

            data.pop(link)
            writing_to_json(data, 'editable/whitelisted_links.json')

            return await ctx.send("Link removed from whitelist")
        except discord.ext.commands.errors.MissingRole:
            return

    @command()
    async def showbl(self, ctx):
      try:
        await commands.has_any_role(bot_commander, another_role, alpha_mod).predicate(ctx)

        with open('editable/blacklisted_links.json') as data_file:
          data = json.load(data_file)

        links = []
        for key, item in data.items():
          links.append(key)

        embed_buider = discord.Embed(title="Blacklisted Links", description='\n'.join(links), color=0x00FF00)
        return await ctx.send(embed=embed_buider)

      except discord.ext.commands.errors.MissingRole:
        return

    @command()
    async def showwl(self, ctx):
      try:
        await commands.has_any_role(bot_commander, another_role, alpha_mod).predicate(ctx)

        with open('editable/whitelisted_links.json') as data_file:
          data = json.load(data_file)

        links = []
        for key, item in data.items():
          links.append(key)

        embed_buider = discord.Embed(title="Whitelisted Links", description='\n'.join(links), color=0x00FF00)
        return await ctx.send(embed=embed_buider)

      except discord.ext.commands.errors.MissingRole:
        return

def writing_to_json(data, file):
    with open(file, 'w') as outfile:
        json.dump(data, outfile, indent=2)


def setup(client):
    client.add_cog(LinkBlacklist(client))
