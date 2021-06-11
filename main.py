import os
import discord 
import json
from discord.ext import commands
from discord import Message, Embed, Colour
from keep_alive import keep_alive  
token = os.environ['token']
client = commands.Bot(command_prefix="!")
with open("json_fields.json", "r") as file:
  content_fields = json.load(file)

#2
@client.command(aliases=()) 
async def ad(ctx):
  field3 = content_fields[2]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)

#3
@client.command(aliases=()) 
async def admin(ctx):
  field3 = content_fields[3]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)

#4
@client.command(aliases=()) 
async def adminshares(ctx):
  field3 = content_fields[4]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)

#5
@client.command(aliases=()) 
async def aero(ctx):
  field3 = content_fields[5]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)

#6
@client.command(aliases=()) 
async def amfdrivers(ctx):
  field3 = content_fields[6]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)

#7
@client.command(aliases=()) 
async def analyze(ctx):
  field3 = content_fields[7]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)

#8
@client.command(aliases=()) 
async def antivirus(ctx):
  field3 = content_fields[8]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)

#9
@client.command(aliases=()) 
async def asio(ctx):
  field3 = content_fields[9]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)

#10
@client.command(aliases=()) 
async def ar(ctx):
  field3 = content_fields[10]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)

#11
@client.command(aliases=()) 
async def audiomonitoring(ctx):
  field3 = content_fields[11]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)

#12
@client.command(aliases=()) 
async def autoconfig(ctx):
  field3 = content_fields[12]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#13
@client.command(aliases=()) 
async def avast(ctx):
  field3 = content_fields[13]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#14
@client.command(aliases=()) 
async def bestsettings(ctx):
  field3 = content_fields[14]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#15
@client.command(aliases=()) 
async def bigsur(ctx):
  field3 = content_fields[15]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#16
@client.command(aliases=()) 
async def blackscreen(ctx):
  field3 = content_fields[16]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)

#16part 2
@client.command(aliases=()) 
async def bs(ctx):
  field3 = content_fields[16]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#17
@client.command(aliases=()) 
async def blame(ctx):
  field3 = content_fields[17]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#18
@client.command(aliases=()) 
async def bluetooth(ctx):
  field3 = content_fields[18]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#19
@client.command(aliases=()) 
async def botrepo(ctx):
  field3 = content_fields[19]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#20
@client.command(aliases=()) 
async def browsersource(ctx):
  field3 = content_fields[20]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#21
@client.command(aliases=()) 
async def buffering(ctx):
  field3 = content_fields[21]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#22
@client.command(aliases=()) 
async def bye(ctx):
  field3 = content_fields[22]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#23
@client.command(aliases=()) 
async def cache(ctx):
  field3 = content_fields[23]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#24
@client.command(aliases=()) 
async def cam(ctx):
  field3 = content_fields[24]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#25
@client.command(aliases=()) 
async def camav(ctx):
  field3 = content_fields[25]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#26
@client.command(aliases=()) 
async def camflip(ctx):
  field3 = content_fields[26]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#27
@client.command(aliases=()) 
async def capturecards(ctx):
  field3 = content_fields[27]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#28
@client.command(aliases=()) 
async def catalina(ctx):
  field3 = content_fields[28]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#29
@client.command(aliases=()) 
async def cert(ctx):
  field3 = content_fields[29]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#30
@client.command(aliases=()) 
async def changelog(ctx):
  field3 = content_fields[30]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#31
@client.command(aliases=()) 
async def chatdocks(ctx):
  field3 = content_fields[31]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#32
@client.command(aliases=()) 
async def chrome(ctx):
  field3 = content_fields[32]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#33
@client.command(aliases=()) 
async def chromeos(ctx):
  field3 = content_fields[33]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#34
@client.command(aliases=()) 
async def classic(ctx):
  field3 = content_fields[34]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#35
@client.command(aliases=()) 
async def cleanlog(ctx):
  field3 = content_fields[35]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#36
@client.command(aliases=()) 
async def cleanprofile(ctx):
  field3 = content_fields[36]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#37
@client.command(aliases=()) 
async def log(ctx):
  field3 = content_fields[37]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#38
@client.command(aliases=()) 
async def logi(ctx):
  field3 = content_fields[38]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#39
@client.command(aliases=()) 
async def commands(ctx):
  field3 = content_fields[39]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#40
@client.command(aliases=()) 
async def conflicts(ctx):
  field3 = content_fields[40]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#41
@client.command(aliases=()) 
async def contributing(ctx):
  field3 = content_fields[41]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#42
@client.command(aliases=()) 
async def converter(ctx):
  field3 = content_fields[42]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#43
@client.command(aliases=()) 
async def coreaudio(ctx):
  field3 = content_fields[43]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#44
@client.command(aliases=()) 
async def cpu(ctx):
  field3 = content_fields[44]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#45
@client.command(aliases=()) 
async def crashlog(ctx):
  field3 = content_fields[45]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#46
@client.command(aliases=()) 
async def crop(ctx):
  field3 = content_fields[46]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#47
@client.command(aliases=()) 
async def crowdin(ctx):
  field3 = content_fields[47]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#48
@client.command(aliases=()) 
async def csgo(ctx):
  field3 = content_fields[48]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#49
@client.command(aliases=()) 
async def cyberpunk2077(ctx):
  field3 = content_fields[49]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#50
@client.command(aliases=()) 
async def delay(ctx):
  field3 = content_fields[50]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#51
@client.command(aliases=()) 
async def dell(ctx):
  field3 = content_fields[51]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#52
@client.command(aliases=()) 
async def deps(ctx):
  field3 = content_fields[52]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#53
@client.command(aliases=()) 
async def destiny2(ctx):
  field3 = content_fields[53]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#54
@client.command(aliases=()) 
async def diagnostic(ctx):
  field3 = content_fields[54]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#55
@client.command(aliases=()) 
async def directx(ctx):
  field3 = content_fields[55]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#57
@client.command(aliases=()) 
async def docki(ctx):
  field3 = content_fields[57]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#58
@client.command(aliases=()) 
async def macdocki(ctx):
  field3 = content_fields[58]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#59
@client.command(aliases=()) 
async def docks(ctx):
  field3 = content_fields[59]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#60
@client.command(aliases=()) 
async def docs(ctx):
  field3 = content_fields[60]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#61
@client.command(aliases=()) 
async def donate(ctx):
  field3 = content_fields[61]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#62
@client.command(aliases=()) 
async def downgrade(ctx):
  field3 = content_fields[62]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#63
@client.command(aliases=()) 
async def download(ctx):
  field3 = content_fields[63]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#64
@client.command(aliases=()) 
async def downtime(ctx):
  field3 = content_fields[64]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#65
@client.command(aliases=()) 
async def dpi(ctx):
  field3 = content_fields[65]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#66
@client.command(aliases=()) 
async def driveby(ctx):
  field3 = content_fields[66]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#67
@client.command(aliases=()) 
async def droste(ctx):
  field3 = content_fields[67]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#68
@client.command(aliases=()) 
async def dslr(ctx):
  field3 = content_fields[68]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#69
@client.command(aliases=()) 
async def ducking(ctx):
  field3 = content_fields[69]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#70
@client.command(aliases=()) 
async def dump(ctx):
  field3 = content_fields[70]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#71
@client.command(aliases=()) 
async def dx12(ctx):
  field3 = content_fields[71]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#72
@client.command(aliases=()) 
async def dynamicbitrate(ctx):
  field3 = content_fields[72]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#73
@client.command(aliases=()) 
async def echo(ctx):
  field3 = content_fields[73]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#74
@client.command(aliases=()) 
async def editor(ctx):
  field3 = content_fields[74]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#75
@client.command(aliases=()) 
async def editors(ctx):
  field3 = content_fields[75]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#76
@client.command(aliases=()) 
async def electron(ctx):
  field3 = content_fields[76]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#77
@client.command(aliases=()) 
async def elgatocrash(ctx):
  field3 = content_fields[77]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#78
@client.command(aliases=()) 
async def elgatodrivers(ctx):
  field3 = content_fields[78]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#79
@client.command(aliases=()) 
async def elgatomac(ctx):
  field3 = content_fields[79]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#80
@client.command(aliases=()) 
async def elgatosupport(ctx):
  field3 = content_fields[80]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#81
@client.command(aliases=()) 
async def english(ctx):
  field3 = content_fields[81]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#82
@client.command(aliases=()) 
async def error(ctx):
  field3 = content_fields[82]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#83
@client.command(aliases=()) 
async def exclusive(ctx):
  field3 = content_fields[83]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#84
@client.command(aliases=()) 
async def export(ctx):
  field3 = content_fields[84]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#85
@client.command(aliases=()) 
async def facebook(ctx):
  field3 = content_fields[85]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#86
@client.command(aliases=()) 
async def facebookbitrate(ctx):
  field3 = content_fields[86]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#87
@client.command(aliases=()) 
async def fider(ctx):
  field3 = content_fields[87]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#88
@client.command(aliases=()) 
async def filters(ctx):
  field3 = content_fields[88]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#89
@client.command(aliases=()) 
async def firefox(ctx):
  field3 = content_fields[89]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#90
@client.command(aliases=()) 
async def flash(ctx):
  field3 = content_fields[90]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#91
@client.command(aliases=()) 
async def fpslimit(ctx):
  field3 = content_fields[91]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#92
@client.command(aliases=()) 
async def connection(ctx):
  field3 = content_fields[92]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#93
@client.command(aliases=()) 
async def free(ctx):
  field3 = content_fields[93]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#94
@client.command(aliases=()) 
async def fullscreen(ctx):
  field3 = content_fields[94]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#95
@client.command(aliases=()) 
async def gamecapture(ctx):
  field3 = content_fields[95]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#96
@client.command(aliases=()) 
async def gamedvr(ctx):
  field3 = content_fields[96]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#97
@client.command(aliases=()) 
async def git(ctx):
  field3 = content_fields[97]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#98
@client.command(aliases=()) 
async def gpl(ctx):
  field3 = content_fields[98]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#99
@client.command(aliases=()) 
async def gpu(ctx):
  field3 = content_fields[99]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#100
@client.command(aliases=()) 
async def gpua(ctx):
  field3 = content_fields[100]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#101
@client.command(aliases=()) 
async def gpuconnection(ctx):
  field3 = content_fields[101]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#102
@client.command(aliases=()) 
async def ddu(ctx):
  field3 = content_fields[102]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#104
@client.command(aliases=()) 
async def gpun(ctx):
  field3 = content_fields[104]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#105
@client.command(aliases=()) 
async def gpuz(ctx):
  field3 = content_fields[105]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#106
@client.command(aliases=()) 
async def greenscreen(ctx):
  field3 = content_fields[106]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#107
@client.command(aliases=()) 
async def hags(ctx):
  field3 = content_fields[107]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#108
@client.command(aliases=()) 
async def hfr(ctx):
  field3 = content_fields[108]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#109
@client.command(aliases=()) 
async def hi(ctx):
  field3 = content_fields[109]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#110
@client.command(aliases=()) 
async def hotkeymode(ctx):
  field3 = content_fields[110]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#111
@client.command(aliases=()) 
async def howtoinstall(ctx):
  field3 = content_fields[111]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#112
@client.command(aliases=()) 
async def hugh(ctx):
  field3 = content_fields[112]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#113
@client.command(aliases=()) 
async def slimport(ctx):
  field3 = content_fields[113]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#114
@client.command(aliases=()) 
async def obsinvite(ctx):
  field3 = content_fields[114]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#115
@client.command(aliases=()) 
async def killernic(ctx):
  field3 = content_fields[115]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#116
@client.command(aliases=()) 
async def kraken(ctx):
  field3 = content_fields[116]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#117
@client.command(aliases=()) 
async def laptop(ctx):
  field3 = content_fields[117]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#118
@client.command(aliases=()) 
async def lastlog(ctx):
  field3 = content_fields[118]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#119
@client.command(aliases=()) 
async def linux(ctx):
  field3 = content_fields[119]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#120
@client.command(aliases=()) 
async def local(ctx):
  field3 = content_fields[120]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#121
@client.command(aliases=()) 
async def localadvanced(ctx):
  field3 = content_fields[121]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#122
@client.command(aliases=()) 
async def loganalyzer(ctx):
  field3 = content_fields[122]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#123
@client.command(aliases=()) 
async def logfolder(ctx):
  field3 = content_fields[123]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#124
@client.command(aliases=()) 
async def logo(ctx):
  field3 = content_fields[124]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#125
@client.command(aliases=()) 
async def lol(ctx):
  field3 = content_fields[125]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#126
@client.command(aliases=()) 
async def m1ndi(ctx):
  field3 = content_fields[126]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#127
@client.command(aliases=()) 
async def mac(ctx):
  field3 = content_fields[127]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#128
@client.command(aliases=()) 
async def macaudio(ctx):
  field3 = content_fields[128]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#129
@client.command(aliases=()) 
async def maccapture(ctx):
  field3 = content_fields[129]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#130
@client.command(aliases=()) 
async def maccrash(ctx):
  field3 = content_fields[130]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#131
@client.command(aliases=()) 
async def macdocks(ctx):
  field3 = content_fields[131]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#132
@client.command(aliases=()) 
async def maclogi(ctx):
  field3 = content_fields[132]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#133
@client.command(aliases=()) 
async def macminimum(ctx):
  field3 = content_fields[133]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#134
@client.command(aliases=()) 
async def macndi(ctx):
  field3 = content_fields[134]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#135
@client.command(aliases=()) 
async def macversions(ctx):
  field3 = content_fields[135]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#136
@client.command(aliases=()) 
async def macpermissions(ctx):
  field3 = content_fields[136]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#137
@client.command(aliases=()) 
async def mantis(ctx):
  field3 = content_fields[137]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#138
@client.command(aliases=()) 
async def manualcam(ctx):
  field3 = content_fields[138]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#139
@client.command(aliases=()) 
async def manualcrash(ctx):
  field3 = content_fields[139]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#140
@client.command(aliases=()) 
async def manuallog(ctx):
  field3 = content_fields[140]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#141
@client.command(aliases=()) 
async def manualpastebin(ctx):
  field3 = content_fields[141]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#142
@client.command(aliases=()) 
async def media(ctx):
  field3 = content_fields[142]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#143
@client.command(aliases=()) 
async def memes(ctx):
  field3 = content_fields[143]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#144
@client.command(aliases=()) 
async def mic(ctx):
  field3 = content_fields[144]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#145
@client.command(aliases=()) 
async def mc(ctx):
  field3 = content_fields[145]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#146
@client.command(aliases=()) 
async def mixer(ctx):
  field3 = content_fields[146]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#147
@client.command(aliases=()) 
async def mobile(ctx):
  field3 = content_fields[147]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#148
@client.command(aliases=()) 
async def mojave(ctx):
  field3 = content_fields[148]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#149
@client.command(aliases=()) 
async def mp4(ctx):
  field3 = content_fields[149]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#150
@client.command(aliases=()) 
async def multirtmp(ctx):
  field3 = content_fields[150]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#151
@client.command(aliases=()) 
async def ndi(ctx):
  field3 = content_fields[151]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#152
@client.command(aliases=()) 
async def ndisdk(ctx):
  field3 = content_fields[152]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#153
@client.command(aliases=()) 
async def nditools(ctx):
  field3 = content_fields[153]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#154
@client.command(aliases=()) 
async def new(ctx):
  field3 = content_fields[154]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#155
@client.command(aliases=()) 
async def newscenecollection(ctx):
  field3 = content_fields[155]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#156
@client.command(aliases=()) 
async def nginx(ctx):
  field3 = content_fields[156]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#157
@client.command(aliases=()) 
async def nightly(ctx):
  field3 = content_fields[157]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#158
@client.command(aliases=()) 
async def nvafx(ctx):
  field3 = content_fields[158]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#159
@client.command(aliases=()) 
async def oc(ctx):
  field3 = content_fields[159]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#160
@client.command(aliases=()) 
async def opengl(ctx):
  field3 = content_fields[160]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#161
@client.command(aliases=()) 
async def params(ctx):
  field3 = content_fields[161]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#162
@client.command(aliases=()) 
async def partial(ctx):
  field3 = content_fields[162]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#163
@client.command(aliases=()) 
async def patreon(ctx):
  field3 = content_fields[163]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#164
@client.command(aliases=()) 
async def pause(ctx):
  field3 = content_fields[164]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#165
@client.command(aliases=()) 
async def periscope(ctx):
  field3 = content_fields[165]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#166
@client.command(aliases=()) 
async def ping(ctx):
  field3 = content_fields[166]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#167
@client.command(aliases=()) 
async def plugins(ctx):
  field3 = content_fields[167]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#168
@client.command(aliases=()) 
async def plugintemplate(ctx):
  field3 = content_fields[168]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#169
@client.command(aliases=()) 
async def portable(ctx):
  field3 = content_fields[169]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#170
@client.command(aliases=()) 
async def portablevc(ctx):
  field3 = content_fields[170]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#171
@client.command(aliases=()) 
async def obspride(ctx):
  field3 = content_fields[171]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#172
@client.command(aliases=()) 
async def programcapture(ctx):
  field3 = content_fields[172]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#173
@client.command(aliases=()) 
async def protectedfolders(ctx):
  field3 = content_fields[173]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#174
@client.command(aliases=()) 
async def quality(ctx):
  field3 = content_fields[174]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#175
@client.command(aliases=()) 
async def quicksync(ctx):
  field3 = content_fields[175]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#176
@client.command(aliases=()) 
async def r6(ctx):
  field3 = content_fields[176]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#177
@client.command(aliases=()) 
async def rc(ctx):
  field3 = content_fields[177]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#178
@client.command(aliases=()) 
async def recordings(ctx):
  field3 = content_fields[178]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#179
@client.command(aliases=()) 
async def recursion(ctx):
  field3 = content_fields[179]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#180
@client.command(aliases=()) 
async def refresh(ctx):
  field3 = content_fields[180]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#181
@client.command(aliases=()) 
async def remote(ctx):
  field3 = content_fields[181]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#182
@client.command(aliases=()) 
async def remotedebugging(ctx):
  field3 = content_fields[182]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#183
@client.command(aliases=()) 
async def remux(ctx):
  field3 = content_fields[183]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#184
@client.command(aliases=()) 
async def replaybuffer(ctx):
  field3 = content_fields[184]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#185
@client.command(aliases=()) 
async def requirements(ctx):
  field3 = content_fields[185]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#186
@client.command(aliases=()) 
async def savage(ctx):
  field3 = content_fields[186]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#187
@client.command(aliases=()) 
async def sceneswitcher(ctx):
  field3 = content_fields[187]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#188
@client.command(aliases=()) 
async def screenshot(ctx):
  field3 = content_fields[188]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#189
@client.command(aliases=()) 
async def scripting(ctx):
  field3 = content_fields[189]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#190
@client.command(aliases=()) 
async def scripts(ctx):
  field3 = content_fields[190]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#191
@client.command(aliases=()) 
async def se(ctx):
  field3 = content_fields[191]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#192
@client.command(aliases=()) 
async def sehelp(ctx):
  field3 = content_fields[192]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#193
@client.command(aliases=()) 
async def settings(ctx):
  field3 = content_fields[193]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#194
@client.command(aliases=()) 
async def shortcuts(ctx):
  field3 = content_fields[194]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#195
@client.command(aliases=()) 
async def sidechain(ctx):
  field3 = content_fields[195]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#196
@client.command(aliases=()) 
async def simple(ctx):
  field3 = content_fields[196]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#197
@client.command(aliases=()) 
async def skype(ctx):
  field3 = content_fields[197]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#198
@client.command(aliases=()) 
async def sl(ctx):
  field3 = content_fields[198]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#199
@client.command(aliases=()) 
async def software(ctx):
  field3 = content_fields[199]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#200
@client.command(aliases=()) 
async def sources(ctx):
  field3 = content_fields[200]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#201
@client.command(aliases=()) 
async def speedtest(ctx):
  field3 = content_fields[201]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#202
@client.command(aliases=()) 
async def srt(ctx):
  field3 = content_fields[202]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#203
@client.command(aliases=()) 
async def stalecookie(ctx):
  field3 = content_fields[203]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#204
@client.command(aliases=()) 
async def streamfx(ctx):
  field3 = content_fields[204]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#205
@client.command(aliases=()) 
async def streamkey(ctx):
  field3 = content_fields[205]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#206
@client.command(aliases=()) 
async def streamreport(ctx):
  field3 = content_fields[206]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#207
@client.command(aliases=()) 
async def studio(ctx):
  field3 = content_fields[207]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#208
@client.command(aliases=()) 
async def support(ctx):
  field3 = content_fields[208]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#209
@client.command(aliases=()) 
async def syphon(ctx):
  field3 = content_fields[209]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#210
@client.command(aliases=()) 
async def testembeds(ctx):
  field3 = content_fields[210]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#211
@client.command(aliases=()) 
async def themes(ctx):
  field3 = content_fields[211]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#212
@client.command(aliases=()) 
async def thiscommanddoesnotexist(ctx):
  field3 = content_fields[212]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#213
@client.command(aliases=()) 
async def timestamps(ctx):
  field3 = content_fields[213]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#214
@client.command(aliases=()) 
async def trackmatte(ctx):
  field3 = content_fields[214]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#215
@client.command(aliases=()) 
async def twitchbitrate(ctx):
  field3 = content_fields[215]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#216
@client.command(aliases=()) 
async def twitchcookie(ctx):
  field3 = content_fields[216]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#217
@client.command(aliases=()) 
async def twitchsoundtrack(ctx):
  field3 = content_fields[217]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#218
@client.command(aliases=()) 
async def twitchtest(ctx):
  field3 = content_fields[218]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#219
@client.command(aliases=()) 
async def twofactor(ctx):
  field3 = content_fields[219]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#220
@client.command(aliases=()) 
async def update(ctx):
  field3 = content_fields[220]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#221
@client.command(aliases=()) 
async def usb(ctx):
  field3 = content_fields[221]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#222
@client.command(aliases=()) 
async def uvc(ctx):
  field3 = content_fields[222]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#223
@client.command(aliases=()) 
async def uwp(ctx):
  field3 = content_fields[223]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#224
@client.command(aliases=()) 
async def vac(ctx):
  field3 = content_fields[224]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#225
@client.command(aliases=()) 
async def vcamaudio(ctx):
  field3 = content_fields[225]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#226
@client.command(aliases=()) 
async def vcamrename(ctx):
  field3 = content_fields[226]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#227
@client.command(aliases=()) 
async def vce(ctx):
  field3 = content_fields[227]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#228
@client.command(aliases=()) 
async def virtualcam(ctx):
  field3 = content_fields[228]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#229
@client.command(aliases=()) 
async def virtualcamremove(ctx):
  field3 = content_fields[229]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#230
@client.command(aliases=()) 
async def virus(ctx):
  field3 = content_fields[230]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#231
@client.command(aliases=()) 
async def vlc(ctx):
  field3 = content_fields[231]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#232
@client.command(aliases=()) 
async def vlcsource(ctx):
  field3 = content_fields[232]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#233
@client.command(aliases=()) 
async def voice(ctx):
  field3 = content_fields[233]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#234
@client.command(aliases=()) 
async def volunteers(ctx):
  field3 = content_fields[234]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#235
@client.command(aliases=()) 
async def prereq(ctx):
  field3 = content_fields[235]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#236
@client.command(aliases=()) 
async def vst(ctx):
  field3 = content_fields[236]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#237
@client.command(aliases=()) 
async def vulkan(ctx):
  field3 = content_fields[237]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#238
@client.command(aliases=()) 
async def websocket(ctx):
  field3 = content_fields[238]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#239
@client.command(aliases=()) 
async def wiki(ctx):
  field3 = content_fields[239]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#240
@client.command(aliases=()) 
async def win10cam(ctx):
  field3 = content_fields[240]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#241
@client.command(aliases=()) 
async def windowsupdate(ctx):
  field3 = content_fields[241]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#242
@client.command(aliases=()) 
async def winsock(ctx):
  field3 = content_fields[242]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#243
@client.command(aliases=()) 
async def workflow(ctx):
  field3 = content_fields[243]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#244
@client.command(aliases=()) 
async def x264(ctx):
  field3 = content_fields[244]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#245
@client.command(aliases=()) 
async def x264presets(ctx):
  field3 = content_fields[245]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#246
@client.command(aliases=()) 
async def xonar(ctx):
  field3 = content_fields[246]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#247
@client.command(aliases=()) 
async def xsplitvcam(ctx):
  field3 = content_fields[247]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#248
@client.command(aliases=()) 
async def yellowborder(ctx):
  field3 = content_fields[248]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#249
@client.command(aliases=()) 
async def younow(ctx):
  field3 = content_fields[249]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#250
@client.command(aliases=()) 
async def youtube(ctx):
  field3 = content_fields[250]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#251
@client.command(aliases=()) 
async def youtubebitrate(ctx):
  field3 = content_fields[251]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)


#252
@client.command(aliases=()) 
async def zerolatency(ctx):
  field3 = content_fields[252]["FIELD3"] 
  embed=discord.Embed(title="", description=field3, color=0x00ff00)
  await ctx.send(embed=embed)

keep_alive()
client.run(token)