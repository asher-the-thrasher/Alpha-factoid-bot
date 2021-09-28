import json
import re

import discord
from discord.ext import commands
from discord.ext.commands import Cog, command
from discord.utils import get

from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow
from discord_slash.context import ComponentContext

from editable.config import configure 
link_role_whitelist=configure.link_role_whitelist 
share_content=configure.share_content
admins=configure.admins

from cogs.mute import create_mute

from utils.bot_log import log_message

blwl = create_select(
    custom_id="blwl",
    options=[  # the options in your dropdown
        create_select_option("Blacklist this", value="blacklist", emoji="👎"),
        create_select_option("Whitelist this", value="whitelist", emoji="👍")
    ],
    placeholder="-- Blacklist or Whitelist --",  # the placeholder text to show when no options have been chosen
    min_values=1,  # the minimum number of options a user must select
    max_values=1,  # the maximum number of options a user can select
)
actions = create_select(
    custom_id="actions",
    options=[  # the options in your dropdown
        create_select_option("Ping Mods", value="ping", emoji="🚨"),
        create_select_option("Allow in Shared Content", value="shareable", emoji="💬")
    ],
    placeholder="-- Select Actions -- (optional)",  # the placeholder text to show when no options have been chosen
    min_values=0,  # the minimum number of options a user must select
    max_values=2,  # the maximum number of options a user can select
)
blwl_selector = create_select(
    custom_id="blwl_selector",
    options=[  # the options in your dropdown
        create_select_option("Show Blacklist", value="blacklist", emoji="⚫"),
        create_select_option("Show Whitelist", value="whitelist", emoji="⚪")
    ],
    placeholder="-- Display Blacklist/Whitelist --",  # the placeholder text to show when no options have been chosen
    min_values=1,  # the minimum number of options a user must select
    max_values=2,  # the maximum number of options a user can select
)

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

        with open('editable/links.json') as json_file:
            data = json.load(json_file)

        # Loops through all disallowed links
        for b_link in data["blacklist"]:
            if b_link["url"] in message.content:
              # Checks if the link is actually allowed
              bad_link = True
              for w_link in data["whitelist"]:
                if b_link["url"] in w_link["url"]:
                  bad_link = False

              # allows certain links to be allowed in a certain channel
              if (message.channel.id == share_content) and (b_link["shareable"] == True):
                bad_link = False

              if bad_link:
                # Establishes a reason for the common ones
                if "twitch.tv/" in b_link:
                  reason_muted = "twitch" 
                elif "discord.gg/" in b_link:
                  reason_muted = "discord"
                else:
                  reason_muted = "blacklisted"

                # To bot log channel

                await log_message(self.bot, f"User Muted (3d) - {reason_muted} link", message.content, message.author, message.channel, moderator=self.bot.user)
                
                try:
                  await message.delete()
                except:
                  continue

                # replaces their message with an embed
                muted_embed = discord.Embed(title="", description=f"{message.author.name} just posted a {reason_muted} link and has been sent to naughty corner to think about what they did.", color = 0xFF0000)
                
                # to channel where blacklisted link was sent
                await message.channel.send(embed=muted_embed)
                
                # mutes
                await create_mute(ctx=message, member=message.author, time="3d", reason="Blacklisted Link")

    @command()
    async def bl(self, ctx, link: str.lower = None):
        if not is_admin(ctx):
          await ctx.send("You can't use that command <:cheems:840763597508313109>")
          return

        if not link:
            return await ctx.send("Please include the blacklisted item after ?bl (ie; ?bl twitch.tv)")

        message = f"**Creating...** *(please work top to bottom)*\n{link}"
        await ctx.send(message, components=[create_actionrow(blwl), create_actionrow(actions)])

    @command()
    async def rem(self, ctx):
        if not is_admin(ctx):
            await ctx.send("You can't use that command <:cheems:840763597508313109>")
            return
        
        with open("editable/links.json") as json_file:
            data = json.load(json_file)

        bl_links = []
        for entry in data["blacklist"]:
            bl_links.append(create_select_option(entry["url"], value=entry["url"], emoji="⚫"))

        wl_links = []
        for entry in data["whitelist"]:
            wl_links.append(create_select_option(entry["url"], value=entry["url"], emoji="⚫"))

        action_row = []
        if len(bl_links) != 0:
            action_row.append(create_actionrow(
                create_select(
                    custom_id="delete_bl",
                    options=bl_links,
                    placeholder="-- Select Options to Remove (Blacklist) --",
                    min_values=0,  # the minimum number of options a user must select
                    max_values=len(bl_links),
                )
            ))

        if len(wl_links) != 0:
            action_row.append(create_actionrow(
                create_select(
                    custom_id="delete_wl",
                    options=wl_links,
                    placeholder="-- Select Options to Remove (Whitelist) --",
                    min_values=0,  # the minimum number of options a user must select
                    max_values=len(wl_links),
                )
            ))

        embed_builder = discord.Embed(title="Click option to remove...")
        await ctx.send(embed=embed_builder, components=action_row)

    @command()
    async def show(self, ctx):
        if not is_admin(ctx):
          await ctx.send("You can't use that command <:cheems:840763597508313109>")
          return

        embed_builder = discord.Embed(title="Show...")
        await ctx.send(embed=embed_builder, components=[create_actionrow(blwl_selector)])

    @Cog.listener()
    async def on_component(self, ctx: ComponentContext):
        #print("RECIEVED")
        if not is_admin(ctx):
          await ctx.send("You can't use that command <:cheems:840763597508313109>")
          return

        with open("editable/links.json") as json_file:
            data = json.load(json_file)

        if ctx.custom_id == "blwl":
            url = str(ctx.origin_message.content).split("\n", 1)[1]
            option = str(ctx.selected_options)[2:-2]

            for string in data[option]:
              if url == string["url"]:
                await ctx.send(f"That link is already in {option}")
                return

            data[option].append({
                "url": url,
                "ping": False,
                "shareable": False
            })

            writing_to_json(data)
            await ctx.send(F"Added to {option}!")

        if ctx.custom_id == "actions":
            url = str(ctx.origin_message.content).split("\n", 1)[1]

            for links in data["blacklist"]:
                if url == links["url"]:
                    links["ping"] = False
                    links["shareable"] = False
                    for options in ctx.selected_options:
                        links[options] = True
                    writing_to_json(data)
                    await ctx.send("Updated Options")
                    return
            for links in data["whitelist"]:
                if url == links["url"]:
                    links["ping"] = False
                    links["shareable"] = False
                    for options in ctx.selected_options:
                        links[options] = True
                    writing_to_json(data)
                    await ctx.send("Updated Options")
                    return

            await ctx.send("Entry was not found, please make sure to select either whitelist or blacklist first")

        if ctx.custom_id == "blwl_selector":
            for option in ctx.selected_options:
                links = []
                for entry in data[option]:
                    links.append(entry["url"])

                embed_builder = discord.Embed(title=f"{option}ed", description='\n'.join(links), color=0x00FF00)
                await ctx.send(embed=embed_builder)

        if ctx.custom_id == "delete_bl":
            for selected in ctx.selected_options:
                for i in range(len(data["blacklist"])):
                    if data["blacklist"][i]["url"] == selected:
                        data["blacklist"].pop(i)
                        break
            writing_to_json(data)
            await ctx.send(f"Deleted {len(ctx.selected_options)} entry(s)!")

        if ctx.custom_id == "delete_wl":
            for selected in ctx.selected_options:
                for i in range(len(data["whitelist"])):
                    if data["whitelist"][i]["url"] == selected:
                        data["whitelist"].pop(i)
                        break
            writing_to_json(data)
            await ctx.send(f"Deleted {len(ctx.selected_options)} entry(s)!")

def writing_to_json(data):
    with open("editable/links.json", 'w') as outfile:
        json.dump(data, outfile, indent=2)

def is_admin(ctx):
  allowed = False
  for roles in admins:
    roles = get(ctx.guild.roles, id=roles)
    role = discord.utils.find(lambda r: r.name == str(roles), ctx.guild.roles)
    
    if role in ctx.author.roles:
      allowed = True
        
  if allowed:
    return True
  else:
    return False

def setup(client):
    client.add_cog(LinkBlacklist(client))
