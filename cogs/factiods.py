import json

import discord
from discord.ext import commands
import os

from editable.config import configure 
another_role=configure.another_role
bot_commander=configure.bot_commander


def writing_to_json(data):
    with open('editable/factoids.json', 'w') as outfile:
        json.dump(data, outfile, indent=2)


async def reload(self):

  for file in os.listdir("cogs"):
    if file.endswith(".py"):
      file = f"cogs.{file[:-3]}"
      self.client.reload_extension(file)

class factoids(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.writing_to_json = writing_to_json

    @commands.command()
    async def add(self, ctx, name: str.lower = None, *, message=None):
        try:
            await commands.has_any_role(bot_commander, another_role).predicate(ctx)
            if name == None:
                return await ctx.send(f'No name specified!')
            if message == None:
                return await ctx.send(f'No message specified!')
            with open("cogs/factoids_execution.py", "r") as fp:
              line_number = 0
              list_of_results = []

              string = f'async def {name}(self,message,*,extra_text=""):'
              for line in fp:
                line_number += 1
                if string in line:
                  list_of_results.append(line_number)
                  



            if list_of_results:
                return await ctx.send(f'The specified name "{name}" already exists as a factoid!')

            with open('editable/factoids.json') as json_file:
                data = json.load(json_file)
            data[f'{name}'] = []
            data[f'{name}'].append({
                'name': f'{name}',
                'content': f'{message}'
            })
            writing_to_json(data)

            with open('cogs/factoids_execution.py') as python_file:
              data = python_file.readlines()
              data[8] = f'''\n    @commands.command(hidden=True)\n    async def {name}(self,message,*,extra_text=""):\n      factoid = """{message}"""\n      await factoids_execution.execute(self, message,factoid,extra_text)\n\n'''
            with open('cogs/factoids_execution.py', 'w') as file:
              file.writelines(data)   


            await ctx.send(f'Factoid "{name}" has been added.')
            await reload(self)
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
            with open("cogs/factoids_execution.py", "r") as fp:
              line_number = 0
              list_of_results = []

              string = f'async def {name}(self,message,*,extra_text=""):'
              for line in fp:
                line_number += 1
                if string in line:
                  list_of_results.append(line_number)
                  



            if not name or not list_of_results:
                return await ctx.send(f'The specified name "{name}" does not exist!')
            name = name


            with open('cogs/factoids_execution.py') as python_file:
              data = python_file.readlines()
              for line in list_of_results:
                del data[line+2]
                del data[line+1]
                del data[line]
                del data[line-1]
                del data[line-2]
            
                

              data[8] = f'''\n    @commands.command(hidden=True)\n    async def {name}(self,message,*,extra_text=""):\n      factoid = """{message}"""\n      await factoids_execution.execute(self, message,factoid,extra_text)\n\n'''
            with open('cogs/factoids_execution.py', 'w') as file:
              file.writelines(data)   


            with open('editable/factoids.json') as data_file:
                data = json.load(data_file)
                data.pop(name)
            writing_to_json(data)




            with open('editable/factoids.json') as json_file:
                data = json.load(json_file)
            data[f'{name}'] = []
            data[f'{name}'].append({
                'name': f'{name}',
                'content': f'{message}'
            })
            writing_to_json(data)


            await ctx.send(f'Factoid "{name}" has been updated.')
            await reload(self)

        except discord.ext.commands.errors.MissingAnyRole:
            await ctx.send('You do not have permissions to use that command')
            return

    @commands.command(name='del')
    async def _del(self, ctx, name: str.lower = None):
        try:
            await commands.has_any_role(bot_commander, another_role).predicate(ctx)
            if name == None:
                return await ctx.send(f'No name specified!')


            with open("cogs/factoids_execution.py", "r") as fp:
              line_number = 0
              list_of_results = []

              string = f'async def {name}(self,message,*,extra_text=""):'
              for line in fp:
                line_number += 1
                if string in line:
                  list_of_results.append(line_number)
                  



            if not name or not list_of_results:
                return await ctx.send(f'The specified name "{name}" does not exist!')
            name = name


            with open('cogs/factoids_execution.py') as python_file:
              data = python_file.readlines()
              for line in list_of_results:
                del data[line+2]
                del data[line+1]
                del data[line]
                del data[line-1]
                del data[line-2]
            with open('cogs/factoids_execution.py', 'w') as file:
              file.writelines(data)  
            name = name
            with open('editable/factoids.json') as data_file:
                data = json.load(data_file)
            data.pop(name)
            writing_to_json(data)


            await ctx.send(f'Factoid "{name}" has been deleted.')
            await reload(self)
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

            with open("cogs/factoids_execution.py", "r") as fp:
              line_number = 0
              list_of_results_name = []

              string = f'async def {name}(self,message,*,extra_text=""):'
              for line in fp:
                line_number += 1
                if string in line:
                  list_of_results_name.append(line_number)

            if not list_of_results_name:
                return await ctx.send(f'The specified name "{name}" does not exist!')
            
            
            with open("cogs/factoids_execution.py", "r") as fp:
              line_number = 0
              list_of_results_new_name = []

              string = f'async def {new_name}(self,message,*,extra_text=""):'
              for line in fp:
                line_number += 1
                if string in line:
                  list_of_results_new_name.append(line_number)

            if list_of_results_new_name:
                return await ctx.send(f'The specified new name "{new_name}" already exist as factoid!')
            

            with open('cogs/factoids_execution.py') as python_file:
              data = python_file.readlines()
              for line in list_of_results_name:
                message = data[line][17:-2]

            name = name
            new_name = new_name
            with open('cogs/factoids_execution.py') as python_file:
              data = python_file.readlines()
              for line in list_of_results_name:
                del data[line+2]
                del data[line+1]
                del data[line]
                del data[line-1]
                del data[line-2]
            
                

              data[8] = f'''\n    @commands.command(hidden=True)\n    async def {name}(self,message,*,extra_text=""):\n      factoid = """{message}"""\n      await factoids_execution.execute(self, message,factoid,extra_text)\n\n'''
            with open('cogs/factoids_execution.py', 'w') as file:
              file.writelines(data)   

            with open('editable/factoids.json') as data_file:
                data = json.load(data_file)
            data.pop(name)
            writing_to_json(data)


            with open('editable/factoids.json') as json_file:
                data = json.load(json_file)
            data[f'{new_name}'] = []
            data[f'{new_name}'].append({
                'name': f'{new_name}',
                'content': f'{message}'
            })
            writing_to_json(data)


            await ctx.send(f'Factoid "{name}" has been renamed to "{new_name}".')
            await reload(self)


        except discord.ext.commands.errors.MissingAnyRole:
            await ctx.send('You do not have permissions to use that command')
            return


def setup(client):
  client.add_cog(factoids(client))
