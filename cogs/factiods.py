import json

import discord
from discord.ext import commands
from replit import db

from editable.config import another_role
from editable.config import bot_commander
from editable.config import command_prefix

from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle

def writing_to_json(data):
    with open('editable/factoids.json', 'w') as outfile:
        json.dump(data, outfile, indent=2)


class factoids(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.writing_to_json = writing_to_json
        self.tator = '<@334067992465899520>'
        self.asher = '<@691724738841804843>'

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.lower().startswith(command_prefix):
            msg_parts = message.content[1:].split()
            factoid_name = msg_parts[0].lower()
            try:
                factoid = db[f"{factoid_name}"]
            except KeyError:
                return

            reference = message.reference
            message_parts = message.content[1:].split()
            # attempt to delete the message requesting the factoid if it's within a reply and only contains command
            if message.reference and len(message_parts) == 1:
                await message.delete(delay=0.0)

            # if users are mentioned (but it's not a reply), mention them in the bot reply as well
            user_mention = None

            if message.mentions and not reference:
                user_mention = ' '.join(user.mention for user in message.mentions)

            embed = discord.Embed(title="", description=factoid, colour=0xf81af3)

            button = False
            if "here]" in factoid.lower():
              button = True

              for words in factoid.split():
                if "here](" in words.lower():
                  if "[here](" in words.lower():
                    url = words[7:]
                  else:
                    url = words[6:]
                  url = url[:-1]

                  actions = create_actionrow(create_button(style=ButtonStyle.URL, url=url, label=f'Click Here'))

            if message.reference and embed is not None:
              if button:
                return await message.channel.send(embed=embed, reference=reference, mention_author=True, components=[actions])
              else:
                return await message.channel.send(embed=embed, reference=reference, mention_author=True)

            elif user_mention and embed is not None:
              if button:
                return await message.channel.send(user_mention, embed=embed, components=[actions])
              else:
                return await message.channel.send(user_mention, embed=embed)

            else:
              if button:
                return await message.channel.send(embed=embed, components=[actions])
              else:
                return await message.channel.send(embed=embed)


        else:
          return


    @commands.command()
    async def add(self, ctx, name: str.lower = None, *, message=None):
        try:
            await commands.has_any_role(bot_commander, another_role).predicate(ctx)
            if name == None:
                return await ctx.send(f'No name specified!')
            if message == None:
                return await ctx.send(f'No message specified!')
            keys = db.keys()

            if name in keys:
                return await ctx.send(f'The specified name "{name}" already exists as a factoid!')

            with open('editable/factoids.json') as json_file:
                data = json.load(json_file)
            data[f'{name}'] = []
            data[f'{name}'].append({
                'name': f'{name}',
                'content': f'{message}'
            })
            writing_to_json(data)

            db[f"{name}"] = f"{message}"

            await ctx.send(f'Factoid "{name}" has been added.')
            channel = self.client.guild.get_channel(863992167264682005)
            return await channel.send(
                f'Factoid "{name}" has been added, please redo the readME.md file and commit and push the changes {self.tator} and {self.asher}.')
        except discord.ext.commands.errors.MissingAnyRole:
            await ctx.send('You do not have permissions to use that command')
            return

    @commands.command()
    async def mod(self, ctx, name: str.lower = None, *, message=None):

        try:
            if name == None:
                return await ctx.send(f'No name specified!')
            if message == None:
                return await ctx.send(f'No message specified!')
            await commands.has_any_role(bot_commander, another_role).predicate(ctx)
            keys = db.keys()
            if not name or name not in keys:
                return await ctx.send(f'The specified name "{name}" does not exist!')
            name = name
            with open('editable/factoids.json') as data_file:
                data = json.load(data_file)
            data.pop(name)
            writing_to_json(data)

            del db[f"{name}"]

            with open('editable/factoids.json') as json_file:
                data = json.load(json_file)
            data[f'{name}'] = []
            data[f'{name}'].append({
                'name': f'{name}',
                'content': f'{message}'
            })
            writing_to_json(data)

            db[f"{name}"] = f"{message}"

            await ctx.send(f'Factoid "{name}" has been updated.')
            channel = self.client.guild.get_channel(863992167264682005)
            return await channel.send(
                f'Factoid "{name}" has been updated, please redo the readME.md file and commit and push the changes {self.tator} and {self.asher}.')
        except discord.ext.commands.errors.MissingAnyRole:
            await ctx.send('You do not have permissions to use that command')
            return

    @commands.command(name='del')
    async def _del(self, ctx, name: str.lower = None):
        try:
            await commands.has_any_role(bot_commander, another_role).predicate(ctx)
            if name == None:
                return await ctx.send(f'No name specified!')
            keys = db.keys()
            if name not in keys:
                return await ctx.send(f'The specified factoid name "{name}" does not exist')

            name = name
            with open('editable/factoids.json') as data_file:
                data = json.load(data_file)
            data.pop(name)
            writing_to_json(data)

            del db[f"{name}"]

            await ctx.send(f'Factoid "{name}" has been deleted.')
            channel = self.client.guild.get_channel(863992167264682005)
            return await channel.send(
                f'Factoid "{name}" has been deleted, please redo the readME.md file and commit and push the changes {self.tator} and {self.asher}.')
        except discord.ext.commands.errors.MissingRole:
            await ctx.send('You do not have permissions to use that command')
            return

    @commands.command()
    async def ren(self, ctx, name: str.lower = None, new_name: str.lower = None):
        try:
            await commands.has_any_role(bot_commander, another_role).predicate(ctx)
            if name == None:
                return await ctx.send(f'No name specified!')
            if new_name == None:
                return await ctx.send(f'No new name specified!')
            keys = db.keys()
            if name not in keys:
                return await ctx.send(f'The specified name "{name}" does not exist!')
            if new_name in keys:
                return await ctx.send(f'The specified new name "{new_name}" already exist as factoid!')
            message = db[f"{name}"]
            name = name
            new_name = new_name

            with open('editable/factoids.json') as data_file:
                data = json.load(data_file)
            data.pop(name)
            writing_to_json(data)

            del db[f"{name}"]

            with open('editable/factoids.json') as json_file:
                data = json.load(json_file)
            data[f'{new_name}'] = []
            data[f'{new_name}'].append({
                'name': f'{new_name}',
                'content': f'{message}'
            })
            writing_to_json(data)

            db[f"{new_name}"] = f"{message}"

            await ctx.send(f'Factoid "{name}" has been renamed to "{new_name}".')
            channel = self.bot.guild.get_channel(863992167264682005)
            return await channel.send(
                f'Factoid "{name}" has been renamed to "{new_name}", please redo the readME.md file and commit and push the changes {self.tator} and {self.asher}.')
        except discord.ext.commands.errors.MissingAnyRole:
            await ctx.send('You do not have permissions to use that command')
            return


def setup(client):
  client.add_cog(factoids(client))
