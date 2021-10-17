import json
from discord.ext.commands import Cog

class configure(Cog):
  with open("editable/config.json") as json_file:
      data = json.loads(json_file.read()) 
  command_prefix = data["command_prefix"]
  bot_activity = data["bot_activity"]



  a_new_testing_server_guild_id = 849649811241173072
  ag_guild_id = 473253164884295699
  guild_id = ag_guild_id
  guild_ids = a_new_testing_server_guild_id,ag_guild_id



  # Role assigned when someone is muted
  a_new_testing_server_muted_role_id = 854885126944587817
  AG_muted_role_id = data["muted_role"]
  Muted_role = AG_muted_role_id


  # Link where certain links are allowed
  AG_share_content_id = data["share_your_content"] 
  a_new_testing_server_share_content_id = 863992156037316648
  share_content = AG_share_content_id


  AG_log_id = data["senpaibot"]
  a_new_testing_server_log_id = 863992167264682005
  log_channel = AG_log_id


  AG_watch_list_id = data["watch_list"] 
  a_new_testing_server_watch_list_id = 881994339184672829
  watch_list = AG_watch_list_id






  # roles that can change the bot
  bot_commander = 730975302167167108
  another_role = 857766098732187658

  # Roles excempt from bot actions
  botadmin = 857766098732187658
  smart_peepo = data["smart_peepo"]
  alpha_mod = data["alpha_mod"]
  unicorn_squad = 599870749271916556
  harris = 473299663718580230
  scott = 847871832383422525
  Sam = 486335848808448000
  Lemonaid = 604482335022514196
  modmod = data["modmod"]

  link_role_whitelist = [botadmin, smart_peepo, alpha_mod, modmod, unicorn_squad, harris, scott, Sam, Lemonaid]

  admins = [botadmin, modmod, unicorn_squad, harris, scott, Sam, Lemonaid]

  # whitelisted channels for log analysis
  general_help = 473309543858962433
  stream_software = 764008007658897439
  pc_help = 599861596159737876
  audio_help = 599861521543200789
  testing_playroom = 744785084313501728
  lights_camera_editing = 599861471874383882
  bot_spam_testing = 849653420544884817
  potato = 857728639613272094

  channel_whitelist = [general_help, stream_software, pc_help, audio_help, testing_playroom, lights_camera_editing, bot_spam_testing, potato]

  # embed color for analysis
  _analysis_colour = 0x5a7474
  mod_color = 0xFF0000

def setup(client):
  client.add_cog(configure(client))
