#https://github.com/codewithswastik/prsaw

from prsaw import RandomStuffV4
from discord.ext.commands import Cog

rs = RandomStuffV4(api_key = 'evsKsqgurfJF')
ai_channels = [904761928684027925,851970921501687828,479468642858434560]
ai_only_channel = 905809995302600754

async def runner(self, message,content):

    response = rs.get_ai_response(content)
    reply = response[0]['message']
    await message.reply(reply)
 


class AI(Cog):
  def __init__(self, client):
    self.client = client
    


  @Cog.listener()
  async def on_message(self, message):
    if message.author.bot:
      return

    if message.channel.id in ai_channels:

      if self.client.user.mentioned_in(message):

        content = message.content.replace(f"<@!{self.client.user.id}>", "")
        
        await runner(self,message,content)
      
      
      #elif message.author.id ==  303469254357942272: #ship
  #      await runner(self, message, message.content)

    if message.channel.id == ai_only_channel:
      await runner(self,message,message.content)
  



def setup(client):
    client.add_cog(AI(client))