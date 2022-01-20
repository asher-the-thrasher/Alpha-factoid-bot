#base code from https://github.com/jnawk/Quart-Discord#basic-example and following docs @ https://discord.com/developers/docs/intro and https://flask-discord.readthedocs.io/en/latest/index.html
from flask import Flask, render_template, redirect, url_for,request
from flask_discord import DiscordOAuth2Session
import os
from threading import Thread
import requests
import json
from utils.website import url_shortener 

from editable.config import Config
guild_ids=Config.guild_ids
admins=Config.admins
botlogerrors = Config.botlogerrors



token = os.environ['token']
client_secret = os.environ['client_secret']
client_id = os.environ['client_id']


myapp = Flask(__name__,template_folder='assets/templates/', static_folder='assets')

myapp.secret_key = "asher"

# # OAuth2 must make use of HTTPS in production environment.

myapp.config["DISCORD_CLIENT_ID"] = client_id    # Discord client ID.
myapp.config["DISCORD_CLIENT_SECRET"] = client_secret            # Discord client secret.
myapp.config["DISCORD_REDIRECT_URI"] = "https://Alpha-Gaming-Factoid-bot.asherthethrashe.repl.co/callback"                 # URL to your callback endpoint.
myapp.config["DISCORD_BOT_TOKEN"] = token                    # Required to access BOT resources.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"
 

discordOAuth = DiscordOAuth2Session(myapp)

def readingjson():
    with open("editable/config.json") as json_file:
        data = json.loads(json_file.read())
        return data

def writingjson(data):
  with open('editable/config.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)


def check():
  in_ag = 0

  if not discordOAuth.authorized:
    in_ag=1
    return in_ag
  user = discordOAuth.fetch_user()
  user_guilds = user.fetch_guilds()
  for guild in user_guilds:
    for guild_id in guild_ids:
      if str(guild.id) == str(guild_id):

        user_request = discordOAuth.bot_request(route=f"/v9/guilds/{guild.id}/members/{user.id}", method='GET')
        user_roles = user_request['roles']

        guild_api = discordOAuth.bot_request(route=f"/v9/guilds/473253164884295699", method='GET')
        guild_roles = guild_api['roles']
        with open('utils/website/assets/templates/role_names.html','w') as file:
            file.write("""{% extends "settings.html" %}\n{% block content %}\n""")
        with open('utils/website/assets/templates/role_names.html','a') as file:
          for guild_role in guild_roles:
            if guild_role['name'] != '@everyone':
        

              file.write(f"<option value='{guild_role['name']}'>{guild_role['name']}</option>\n")
            
          file.write("{% endblock %}")
        for role in user_roles: 
          for admin in admins:
            if str(role) == str(admin):
              in_ag = 2
  return in_ag


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

@myapp.route("/commands")
def commands():
  return render_template("commads.html")

    
@myapp.route("/support")
def support():
  return render_template("support.html")

@myapp.route("/dashboard/")
def dashboard():
  in_ag = check()
  if in_ag == 1:
    return redirect(url_for("login"))
  elif in_ag == 0:
    return render_template("missing_access.html")
  elif in_ag == 2:
    return redirect(url_for('home'))

@myapp.route("/testing")
def test():
  return render_template("f.html")


@myapp.errorhandler(404)
def not_found(e):
  return render_template("404.html")




@myapp.route('/settings', methods=['GET', 'POST'])
def settings():
  in_ag = check()
  if in_ag == 1:
    return redirect(url_for("login"))
  elif in_ag == 0:
    return render_template("missing_access.html")
  elif in_ag == 2:


    if request.method == 'GET':
        data = readingjson()

        return render_template('role_names.html', bot_prefix = data["command_prefix"],bot_commander=data['bot_commander'])


    if request.method == 'POST':
      form_name = request.form['form-name']

      if form_name == 'EmergencyButton':

        baseURL = "https://discordapp.com/api/channels/{}/messages".format(botlogerrors)
        headers = { "Authorization":"Bot {}".format(token),
            "User-Agent":"myBotThing (http://some.url, v0.1)",
            "Content-Type":"application/json", }

        message = "<@!691724738841804843> replit exited through website"

        POSTedJSON = json.dumps ( {"content":message} )

        requests.post(baseURL, headers = headers, data = POSTedJSON)

        print(message)
        os._exit(1)



      if form_name == 'botcommander':
        data = readingjson()
        new_commander = (request.form)['new_commander']
        

        data["bot_commander"]=new_commander
        writingjson(data)
        
        return render_template('role_names.html', bot_prefix = data["command_prefix"],bot_commander=data['bot_commander'])


      if form_name == 'prefix': 
        data = readingjson()
        prefix = (request.form)['prefix']
        data["command_prefix"]=prefix
        writingjson(data)

        return render_template('role_names.html', bot_prefix = data["command_prefix"],bot_commander=data['bot_commander'])


@myapp.route("/url", methods=['GET', 'POST'])
def url_shorten():
  


  if request.method == 'GET':

    return render_template('url.html')

  if request.method == 'POST':
    form_name = request.form['form-name']

    if form_name == 'url_shortener':
      url = (request.form)['url_shortener']
      return redirect(f'/url/shorten/?url={url}')

@myapp.route("/url/shorten/", methods=['GET', 'POST'])
def url_shortening():
  if request.method == 'GET':
    url = request.args.get('url')
    print(url)
    url1 = url_shortener.shortener(url)
    print(url1)
    return render_template('shortened_url.html',short_url=url1)
      

    
@myapp.route("/<site>")
def rest_of_site(site):
    return render_template("404.html")






def run():
  myapp.run(host='0.0.0.0',port=8080)


def website():
    t = Thread(target=run)
    t.start()



