#base code from https://github.com/jnawk/Quart-Discord#basic-example and following docs @ https://discord.com/developers/docs/intro and https://flask-discord.readthedocs.io/en/latest/index.html
from flask import Flask, render_template, redirect, url_for,request
from flask_discord import DiscordOAuth2Session
import os
from threading import Thread
import json

from editable.config import configure
guild_ids=configure.guild_ids
admins=configure.admins


token = os.environ['token']
client_secret = os.environ['client_secret']
client_id = os.environ['client_id']


myapp = Flask(__name__,template_folder='assets/templates/', static_folder='assets')

myapp.secret_key = "asher"

# # OAuth2 must make use of HTTPS in production environment.

myapp.config["DISCORD_CLIENT_ID"] = client_id    # Discord client ID.
myapp.config["DISCORD_CLIENT_SECRET"] = client_secret            # Discord client secret.
myapp.config["DISCORD_REDIRECT_URI"] = "https://senpaibot.asherthethrashe.repl.co/callback"                 # URL to your callback endpoint.
myapp.config["DISCORD_BOT_TOKEN"] = token                    # Required to access BOT resources.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"
 

discordOAuth = DiscordOAuth2Session(myapp)

@myapp.route("/home")
def home():
  return render_template("index.html", authorized = discordOAuth.authorized)


@myapp.route("/")
def base():
  return redirect(url_for('home'))


@myapp.route("/login/")
def login():
  return discordOAuth.create_session(scope=["identify", "guilds"])

@myapp.route("/callback/")
def callback():
  try:
    discordOAuth.callback()
  except Exception:
    pass
  return redirect(url_for("dashboard"))

@myapp.route("/<site>")
def rest_of_site(site):
  if not discordOAuth.authorized:
    return redirect(url_for("login"))
  try:
    return render_template(f"{site}.html")
  except:
    return render_template("404.html")

    


@myapp.route("/dashboard/")
def dashboard():
  if not discordOAuth.authorized:
    return redirect(url_for("login"))
  user = discordOAuth.fetch_user()
  user_guilds = user.fetch_guilds()
  in_ag = False
  for guild in user_guilds:
    for guild_id in guild_ids:
      if str(guild.id) == str(guild_id):

        user_request = discordOAuth.bot_request(route=f"/v9/guilds/{guild.id}/members/{user.id}", method='GET')
        user_roles = user_request['roles']
        for role in user_roles: 
          for admin in admins:
            if str(role) == str(admin):
              print(str(user))
              in_ag = True

  in_ag = True
  if in_ag:
    return redirect(url_for('home'))
  if not in_ag:
    discordOAuth.authorized = False
    return render_template('missing_access.html')



@myapp.errorhandler(404)
def not_found(e):

  return render_template("404.html")




@myapp.route('/settings', methods=['GET', 'POST'])
def settings():
    if not discordOAuth.authorized:
      return redirect(url_for("login"))
    user = discordOAuth.fetch_user()
    user_guilds = user.fetch_guilds()
    in_ag = False
    for guild in user_guilds:
      for guild_id in guild_ids:
        if str(guild.id) == str(guild_id):

          user_request = discordOAuth.bot_request(route=f"/v9/guilds/{guild.id}/members/{user.id}", method='GET')
          user_roles = user_request['roles']
          for role in user_roles: 
            for admin in admins:
              if str(role) == str(admin):
                print(str(user))
                in_ag = True

    if not in_ag:
      return render_template("missing_access.html")
    if request.method == 'GET':
      with open("editable/config.json") as json_file:
        data = json.loads(json_file.read()) 
        bot_prefix = data["command_prefix"]
        return render_template('settings.html', bot_prefix = bot_prefix)

    prefix = (request.form)['prefix']
    print(prefix)
    with open("editable/config.json") as json_file:
      data = json.loads(json_file.read()) 
      data["command_prefix"]=prefix
      with open('editable/config.json', 'w') as outfile:
        json.dump(data, outfile, indent=2)

    return render_template('settings.html',bot_prefix = prefix)


def run():
  myapp.run(host='0.0.0.0',port=8080)


def website():
    t = Thread(target=run)
    t.start()
