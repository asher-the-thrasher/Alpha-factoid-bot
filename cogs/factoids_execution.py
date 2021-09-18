import discord
from discord.ext import commands
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle


class factoids_execution(commands.Cog):  


    @commands.command()
    async def dblevel(self,message,*,extra_text=""):
      factoid = """**How to get to the levels tab and set to decibels in Windows**
Windows button > type "change system sounds" > recording tab > select your mic > go to properties > levels tab > right click the blue slider > change to decibels.

Post a screenshot after."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def top5q(self,message,*,extra_text=""):
      factoid = """**Harris Heller's Top 5 Terrible FAQs**
__Should I go full time?__
https://youtu.be/OGOtnO2zwfg?t=154

__Which platform should I stream on?__
https://youtu.be/OGOtnO2zwfg?t=283

__Should I buy A or B?__
https://youtu.be/OGOtnO2zwfg?t=366

__Should I buy a webcam or a full camera?__
https://youtu.be/OGOtnO2zwfg?t=406

__Should I show my face on cam?__
https://youtu.be/OGOtnO2zwfg?t=506"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def me(self,message,*,extra_text=""):
      factoid = """me"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def gpu(self,message,*,extra_text=""):
      factoid = """If you are experiencing issues with performance while playing games, or just in general while using OBS, your GPU may be overloaded for the settings you are trying to use. Please check our GPU overload guide for ideas why this may be happening, and steps you can take to correct it. [Click here](https://obsproject.com/wiki/GPU-overload-issues) for guide"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command(name="900p")
    async def _900p(self,message,*,extra_text=""):
      factoid = """Streaming at 900p is not recommended as the twitch player cannot properly handle it. [Click here](https://www.reddit.com/r/Twitch/comments/fx5wbc/fix_strange_lines_on_stream/) for more information. It is recommended to stick to 720p or 1080p or if you really must 936p or 864p."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def invite(self,message,*,extra_text=""):
      factoid = """https://discord.gg/alphagaming"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def blame(self,message,*,extra_text=""):
      factoid = """It's Dagaz's fault."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def editors(self,message,*,extra_text=""):
      factoid = """Hi, for a list of software you can use to edit photos and videos or create designs, [Click Here](https://discord.com/channels/473253164884295699/788520412299395114/788572536925323275)
Happy editing!"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def connect(self,message,*,extra_text=""):
      factoid = """[click here](https://www.youtube.com/watch?v=sQnhk2JIeGs) to connect your twitch to discord"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def collab(self,message,*,extra_text=""):
      factoid = """Hi to find collab partners, or even just others to game with, head to <#526512748604031027> ! If you can't see it, that's because you don't have the Content Creator role yet. Go to <#827759085280690197> and follow the instructions  😉"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def credit(self,message,*,extra_text=""):
      factoid = """Many of the commands in this server are from the OBS Studio Discord, we appreciate them for allowing us to use their commands!"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command(name="commands")
    async def _commands(self,message,*,extra_text=""):
      factoid = """A list of commands can be found [here](https://asher-the-thrasher.github.io/Alpha-factoid-bot/)"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def volunteers(self,message,*,extra_text=""):
      factoid = """The Alpha Gaming discord server support is provided for free by community volunteers in their spare time."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def mc(self,message,*,extra_text=""):
      factoid = """To capture Minecraft Java Edition, make sure the Game Capture "Mode" is set to "Capture specific window", and select javaw/minecraft in the "Window" drop down.
If you are still having issues please follow our [Minecraft capture guide](https://obsproject.com/wiki/Minecraft-Not-Working-With-Game-Capture)"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def macversions(self,message,*,extra_text=""):
      factoid = """For High Sierra (10.13) & newer, use OBS Studio 25+ (recommended)
Older versions
Update macOS if you can. We no longer provide support for these older versions.
For Sierra (10.12), use OBS 24.0.6
For El Capitan (10.11), use OBS 21.1.1
For Yosemite (10.10), use OBS 20.1.0"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def laptop(self,message,*,extra_text=""):
      factoid = """If you're using OBS Studio 27+ on Windows 10 1809 or earlier, your system must be configured to run OBS on a specific GPU, depending on the type of capture you are trying to do.
[Click here](https://obsproject.com/wiki/Laptop-Troubleshooting) for instructions on how to configure your system."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def dropped(self,message,*,extra_text=""):
      factoid = """Dropped frames? Disconnecting?
Follow the troubleshooting steps in our [Connection Issues guide](https://obsproject.com/wiki/Dropped-Frames-and-General-Connection-Issues)."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def english(self,message,*,extra_text=""):
      factoid = """Welcome to the official Alpha Gaming Community Discord server! Unfortunately, our support volunteers can only provide support in English. Most of our support documents and guides are also only in English. If you feel comfortable using a service like Google Translate, feel free to use that to send messages to us. We'll do our best to understand your intent, and we'll try to help you as much as we can. [Translate](https://translate.google.com/?sl=en&tl=es&text=Welcome%20to%20the%20official%20Alpha%20Gaming%20Community%20Discord%20server!%20Unfortunately%2C%20our%20support%20volunteers%20can%20only%20provide%20support%20in%20English.%20Most%20of%20our%20support%20documents%20and%20guides%20are%20also%20only%20in%20English.%20If%20you%20feel%20comfortable%20using%20a%20service%20like%20Google%20Translate%2C%20feel%20free%20to%20use%20that%20to%20send%20messages%20to%20us.%20We%27ll%20do%20our%20best%20to%20understand%20your%20intent%2C%20and%20we%27ll%20try%20to%20help%20you%20as%20much%20as%20we%20can.&op=translate) """
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def macdocki(self,message,*,extra_text=""):
      factoid = """https://i.imgur.com/DbpZ44G.png """
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def bt(self,message,*,extra_text=""):
      factoid = """If your audio is muting when you launch OBS, and you're using a Bluetooth headset, it's caused by the underlying design of Bluetooth. To fix this, you can either switch to a wired headset, don't use the Bluetooth headset's mic, or set your sound to go through the HFP device for your headset.
Note: HFP offers lower sound quality."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def bs(self,message,*,extra_text=""):
      factoid = """If you are trying to stream or record with OBS and are getting a black screen, make sure you have added the appropriate source to capture what you are trying to show. Window, Game, and Display capture are the three most common capture sources. If you have already added a capture source, and OBS is still black, please grab your current log and link it here.
Help -> Log Files -> Upload Current Log!"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def am(self,message,*,extra_text=""):
      factoid = """To use the Audio Monitoring feature, click Edit -> Advanced Audio Properties and set Audio Monitoring to either Monitor Only, or Monitor and Output. Monitor Only will not output that device's audio to your stream/recording.
Audio for that device will be played out of your system default device, unless otherwise specified in Settings -> Audio -> Advanced."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def ar(self,message,*,extra_text=""):
      factoid = """Black bars on your stream or recording? Read How to select the correct Aspect Ratio for your Recording/Stream and How to do a 16:9 stream with any size of Video-input."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def logi(self,message,*,extra_text=""):
      factoid = """https://i.imgur.com/oL0BZjn.png"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def log(self,message,*,extra_text=""):
      factoid = """A current log file is required to help fix your issue. Please post a link to your current log file.
In OBS select Help > Log Files > Upload Current Log File.
Click Copy URL and then paste the link here."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def report(self,message,*,extra_text=""):
      factoid = """**How to Make a Server Report**
Reports should be made in #┃reports-server-issues To make a server report you will need: 
- A screenshot of the problem interaction 
- The user's ID (not their tag)* 

* If you're not sure how to get the user ID, here's a quick guide: https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-I     

Thank you for helping to improve our server!"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def variables(self,message,*,extra_text=""):
      factoid = """[Click Here](https://discord.com/channels/473253164884295699/473309543858962433/726223921489248276) for a list of all the Variables for the Alpha Rotating Feed"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def streambeats(self,message,*,extra_text=""):
      factoid = """Hi, for all things Streambeats, including the link to the Streambeats server, [Click Here](https://discord.com/channels/473253164884295699/703808841829318657/789675905647378442)"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def specs(self,message,*,extra_text=""):
      factoid = """[Click Here](https://discord.com/channels/473253164884295699/473309543858962433/827291094625943622) and follow this guide to find out what CPU and GPU you have!"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def sampai(self,message,*,extra_text=""):
      factoid = """Hi, you can [click here](https://discord.com/channels/473253164884295699/595049244801630248/716746628232380588) to find the invite to Sam's server!
"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def goxlr(self,message,*,extra_text=""):
      factoid = """Hi! For a link to a quick FAQ of GoXLR stuffs [click here](https://discord.com/channels/473253164884295699/599861521543200789/831288085798453258)"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def pixelchat(self,message,*,extra_text=""):
      factoid = """For detailed instructions on how to set up the Now Playing Widget on Pixelchat, [click here](https://discord.com/channels/473253164884295699/764008007658897439/780348277853650957)"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def nvenc(self,message,*,extra_text=""):
      factoid = """Hi! You can find the basic NVENC settings for OBS Recording and Twitch Streaming [here](https://discord.com/channels/473253164884295699/764008007658897439/806313313146372117)"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def lights(self,message,*,extra_text=""):
      factoid = """Hi! You can check out our recommended lights [here](https://discord.com/channels/473253164884295699/599861471874383882/780085668202151976). This list may be updated sometimes, so check back if you need! """
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def grow(self,message,*,extra_text=""):
      factoid = """Hi, 

Since Twitch has horrible discoverability, you're going to find it very hard to grow from streaming alone. You need to be making content on other, more discoverable platforms and funnel those viewers to Twitch. 
Platforms like YouTube (YT, FB, TikTok, etc) help grow your brand and create an interest in you and/or your content hanging out with you in a live stream. 

Live interaction is Twitch's strength, so you'd need to see the strengths and weaknesses of each platform, and use them accordingly. 

_Here are some Alpha Gaming Vids to watch if you haven't already:_
- 25 Twitch Tips in 10 mins: https://www.youtube.com/watch?v=si7VS8dVSZA 
- Top 5 Streaming Mistakes: https://www.youtube.com/watch?v=8tjJpUkGGBw"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def cliffnotes(self,message,*,extra_text=""):
      factoid = """_CLIFF NOTES_
- ISO as low as possible (iso should ideally be under 800, if that's too dark you need more light) 
- aperture (f) as wide open as possible (with kit lens) 
- shutter speed twice the fps 
- custom white balance 
- make sure your camera is in movie mode 
- don't leave anything on auto"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def c920(self,message,*,extra_text=""):
      factoid = """_C920/C922/C930e Best Practices_
 - Exposure should be set to between -7 and -5 
- Low Light comp should be turned to off
- Gain should be 0 
- White balance should be where your skintones are normal 
- Add a touch of sharpening from default (between 128 and 140) 
- Add a touch of contrast from default (between 128 and 140)
- Add a touch of sat from default (between 128 and 140)
- Add some brightness if the darks are a bit too dark"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def alphawidget(self,message,*,extra_text=""):
      factoid = """Hi, you can access the Sub Train and Rotating Feed Widgets [here!](https://discord.com/channels/473253164884295699/473299541999878144/604726378025320523)"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def rule6(self,message,*,extra_text=""):
      factoid = """__**REMINDER:**__ This is not a marketplace server. We do not allow offering or soliciting of transactions (paid or otherwise) on this server. If two people come to an agreement via DMs to go around this rule, then please note that this is at your own risk. The server is _NOT_ liable for any issues you may face from these transactions.

If you need an artist, we recommend searching on a proper platform such as Fiverr or 99designs, or even Twitter. 


PS. Don't ask someone to make you something for free. If you want to learn how to make things yourself, the community is more than willing to help you if you need pointers or specific help with techniques."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def pokemon(self,message,*,extra_text=""):
      factoid = """Hi! We're sorry to tell you that If you're looking for the Pokémon sound files, they've been removed to avoid potential copyright issues."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def zerolatency(self,message,*,extra_text=""):
      factoid = """https://cdn.knightlab.com/libs/juxtapose/latest/embed/index.html?uid=a8cb00ac-55c9-11eb-83c8-ebb5d6f907df"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def youtubebitrate(self,message,*,extra_text=""):
      factoid = """You can find YouTube's recommended bitrates for different resolutions here: https://support.google.com/youtube/answer/2853702?hl=en
Keep in mind that unlike Twitch, YouTube re-encodes your original stream resolution, so you may need a higher bitrate to match the quality you'd normally see. Aim for the higher values in the ranges suggested by YouTube."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def youtube(self,message,*,extra_text=""):
      factoid = """How to stream to YouTube: https://obsproject.com/forum/resources/streaming-to-youtube-with-obs-studio.232/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def younow(self,message,*,extra_text=""):
      factoid = """YouNow is not compatible with OBS Studio from obsproject.com.
You will have to use their fork for which we can't provide support.
Please see https://younow.zendesk.com/hc/articles/206439166"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def yellowborder(self,message,*,extra_text=""):
      factoid = """When using a Window Capture source with the Windows Graphics Capture (WGC) method, or a Display Capture source with the Windows 10 1903+ method, you will have a yellow border surrounding the portion of the screen being captured. Unfortunately, this border cannot currently be removed, as the Windows SDK does not allow it. You can try using another capture method in the source properties, but it's possible this will instead produce a black screen. Once Microsoft release an update to the Windows SDK that allow us to disable the yellow border, we will be sure to let you turn off the border."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def xsplitvcam(self,message,*,extra_text=""):
      factoid = """The XSplit VCam allows you to remove or blur the background of your webcam without needing a greenscreen or other expensive hardware.
You can check it out here: [XSplit VCam](https://www.xsplit.com/partners/obs)
As part of the sponsorship to OBS, the team at XSplit is donating a portion of the proceeds from VCam back to OBS!"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def xonar(self,message,*,extra_text=""):
      factoid = """If you are using an Asus Xonar sound device, you will need to disable GX mode in its software and reboot your PC."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def x264presets(self,message,*,extra_text=""):
      factoid = """When streaming, you can set the x264 preset to a slower sounding value for increased quality, at the cost of increased CPU usage. It is recommended to leave this value on veryfast, as there are significant diminishing returns to setting it lower. See here for a comparison: https://r-1.ch/x264_preset_comparison/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def x264(self,message,*,extra_text=""):
      factoid = """An introductory guide to streaming with the x264 encoder can be found on the OBS Development Blog here: https://obsproject.com/blog/streaming-with-x264"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def workflow(self,message,*,extra_text=""):
      factoid = """https://imgs.xkcd.com/comics/workflow.png"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def winsock(self,message,*,extra_text=""):
      factoid = """https://docs.microsoft.com/en-us/windows/win32/winsock/windows-sockets-error-codes-2"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def windowsupdate(self,message,*,extra_text=""):
      factoid = """If you've installed the Visual C++ Components that OBS Studio requires, but still aren't able to install OBS Studio, you may need to update your Windows installation. To do this, follow these steps.
1) Open Windows Update. This can be found by searching for Windows Update in the Start Menu, or in the Control Panel.
2) Install any available updates.
3) Restart your PC to finish installing updates.
4) Repeat steps 1-3 until there are absolutely 0 updates remaining.
Once Windows is fully up to date, try installing OBS again. If that doesn't work, install the UCRT manually: https://support.microsoft.com/en-us/help/3118401/update-for-universal-c-runtime-in-windows"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def win10cam(self,message,*,extra_text=""):
      factoid = """Windows 10's April 2018 Update adds new privacy settings for microphones and cameras, which can block them from use. The camera privacy settings also affect capture cards. These settings are opt-in. To allow apps like OBS to use your microphone or camera again, follow these steps.
1) Open the Settings app.
2) Go to Privacy -> Camera for capture cards and webcams, and turn "Allow apps to access your camera" on.
3) Go to Privacy -> Microphones, and turn "Allow apps to access your microphone" on."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def wiki(self,message,*,extra_text=""):
      factoid = """To see all of our guides, or to generally get a better understanding of OBS, check out the wiki: https://obsproject.com/wiki/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def websocket(self,message,*,extra_text=""):
      factoid = """A plugin for controlling OBS via websockets is available here:
OBS Websockets"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def vulkan(self,message,*,extra_text=""):
      factoid = """As of OBS v25, Vulkan capture is natively supported on Windows."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def vst(self,message,*,extra_text=""):
      factoid = """OBS Studio supports most VST2 plugins. More information can be found here, including restrictions and plugin install paths: https://obsproject.com/wiki/Filters-Guide#vst-plugin"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def vs2017(self,message,*,extra_text=""):
      factoid = """Visual Studio 2019 runtimes are required by the plugins that come with OBS Studio.
Download and install both vc2019redist_x86.exe and vc2019redist_x64.exe from https://obsproject.com/visual-studio-2019-runtimes"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def voice(self,message,*,extra_text=""):
      factoid = """A basic guide to improve your microphone quality can be found here: https://obsproject.com/forum/resources/514/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def vlcsource(self,message,*,extra_text=""):
      factoid = """VLC source requires VLC to be installed on your system, with the correct bitness. 32-bit VLC for 32-bit OBS, or 64-bit VLC for 64-bit OBS.
VLC can be downloaded here: http://www.videolan.org/vlc/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def vlc(self,message,*,extra_text=""):
      factoid = """Many default video players do not have good format support. When playing files made with OBS, players like 'Movies & TV' can appear to be missing video or audio. [Download and use VLC](https://www.videolan.org/vlc/index.html) instead for accurate video playback.
Like OBS, VLC is a free and open source project."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def virus(self,message,*,extra_text=""):
      factoid = """OBS Studio is guaranteed to be completely virus and malware free, as long as you download it from the official website at https://obsproject.com/download"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def virtualcamremove(self,message,*,extra_text=""):
      factoid = """To uninstall VirtualCam on Windows:
1) Navigate to: C:\Program Files\obs-studio\data\obs-plugins\win-dshow
2) Right click virtualcam-uninstall.bat, and Run as Administrator.
If you have OBS installed in a different directory (or in portable mode), right click your OBS shortcut and choose "Open file location" to track down the location of the obs-studio directory."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def virtualcam(self,message,*,extra_text=""):
      factoid = """Windows: OBS v26 and above contains a basic virtual camera. For advanced usage, such as preview or specific scene/source output, try the [third party plugin](https://obsproject.com/forum/resources/obs-virtualcam.949/).
macOS: OBS v26.1 and above contains a standard virtual camera. Having issues with specific programs? Check [this guide](https://obsproject.com/wiki/MacOS-Virtual-Camera-Compatibility-Guide).
Linux: OBS v26.1 and above contains a standard virtual camera. v4l2loopback is required, best installed via the v4l2loopback-dkms package."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def vce(self,message,*,extra_text=""):
      factoid = """The AMD Advanced Media Framework (VCE) encoder plugin is available in OBS Studio as part of the base installation on Windows. If you are having issues using this encoder, first make sure that your drivers are [fully up to date.](https://support.amd.com/en-us/download)
If updating both drivers and plugin does not work, check the [troubleshooting guide.](https://github.com/obsproject/obs-amd-encoder/wiki/Guide%3A-Troubleshooting)"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def vcamrename(self,message,*,extra_text=""):
      factoid = """The virtual camera device from OBS cannot be renamed. Even if it was to be renamed, it wouldn't allow applications to use it any differently. If an application is blocking the virtual camera, it would still be blocked."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def vcamaudio(self,message,*,extra_text=""):
      factoid = """Install [VB-Audio CABLE](https://www.vb-audio.com/Cable/index.htm). (A reboot is not required)
In OBS Studio, go to Settings > Audio and select "CABLE Input" as your Monitoring Device
Go to Edit > Advanced Audio Properties and enable Audio Monitoring for the audio sources you'd like to stream to Discord.
In Discord, in Voice & Video settings, select "CABLE Output" instead of your microphone under "Input device".
Now anything you monitor in OBS Studio will be streamed to Discord. Similar steps will work with other conferencing apps, such as Microsoft Teams or Slack."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def vac(self,message,*,extra_text=""):
      factoid = """How to exclude or separate audio sources for a stream or recording: https://obsproject.com/forum/resources/8/
For a more advanced setup, check out our guide on [Voicemeeter Banana](https://canary.discord.com/channels/473253164884295699/599861521543200789/801271416817319966)"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def uwp(self,message,*,extra_text=""):
      factoid = """As of 25.0.8, manual action is no longer required to capture UWP games. If you're still having trouble, try running OBS as Administrator, or check our list of conflicting apps."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def uvc(self,message,*,extra_text=""):
      factoid = """Here’s how to install native UVC drivers for your webcam:
Open Device Manager.
Expand Imaging devices.
Locate the name of your camera in the list and right-click on it.
Select Update Driver Software…
Click Browse my computer for driver software.
Click Let me pick from a list of device drivers on my computer.
Check Show compatible hardware, and then select USB Video Device.
Click Next and follow the on-screen instructions to update the driver."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def usb(self,message,*,extra_text=""):
      factoid = """USB problems? Use the USBView program to identify which hubs your devices are connected to. Move bandwidth-hungry devices like webcams and capture cards to separate hubs by switching their USB ports."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def update(self,message,*,extra_text=""):
      factoid = """Having issues updating OBS? Make sure OBS and any applications/games that were being captured are closed before trying to run the update. Still getting an error? Reboot your PC and run the installer again. Be sure not to open OBS until after the install finishes."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def twofactor(self,message,*,extra_text=""):
      factoid = """If you are having issues streaming to Twitch recently, please make sure two-factor authentication is set up in your Twitch security settings as this is now required to stream."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def twitchtest(self,message,*,extra_text=""):
      factoid = """Use the Twitch Bandwidth Test to find the best Twitch server to stream to. Set Duration to Medium. You can uncheck any regions you're not near. After the test completes, click the Share Result button to upload a screenshot, which can then be copied and pasted here. Get TwitchTest from https://r1ch.net/projects/twitchtest"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def twitchsoundtrack(self,message,*,extra_text=""):
      factoid = """To correctly configure Soundtrack by Twitch, please follow [their guide](https://help.twitch.tv/s/article/soundtrack-audio-configuration)."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def twitchcookie(self,message,*,extra_text=""):
      factoid = """To fix the Twitch cookie message in OBS panels, go to Settings > Stream and logout of your Twitch account, then login again."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def twitchbitrate(self,message,*,extra_text=""):
      factoid = """You can find Twitch's recommended bitrates for different resolutions here: https://stream.twitch.tv/encoding/
Keep in mind that you shouldn't go above 6000 Kbps, and if you're not partnered don't set your bitrate too high otherwise your viewers may have trouble watching your stream."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def trackmatte(self,message,*,extra_text=""):
      factoid = """For more information on how to create and use track matte stinger transitions, read our guide on the [wiki](https://obsproject.com/wiki/Getting-Started-With-Track-Matte-Stinger-Transitions)."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def timestamps(self,message,*,extra_text=""):
      factoid = """Some audio devices do not send proper timestamps, and can cause various issues, such as audio desync. Try disabling the device timestamps in OBS by clicking the Gear icon next to your audio source, select Properties, and then uncheck 'Use device timestamps.''"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def thiscommanddoesnotexist(self,message,*,extra_text=""):
      factoid = """this command does not exist"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def themes(self,message,*,extra_text=""):
      factoid = """OBS Studio supports custom themes!
Download user made themes: https://obsproject.com/forum/resources/categories/10/
Learn to make your own themes and where to install themes: https://obsproject.com/wiki/Custom-Themes"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def testembeds(self,message,*,extra_text=""):
      factoid = """None"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def syphon(self,message,*,extra_text=""):
      factoid = """Quick instructions on how to use Syphon capture for games on macOS: https://gist.github.com/Fenrirthviti/ff3d52245046e831f0f2983bcf4c54db"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def support(self,message,*,extra_text=""):
      factoid = """Please use one of the Get Help channels for help, if you are unsure of which catagory to ask in, ask in <#473309543858962433> first!"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def studio(self,message,*,extra_text=""):
      factoid = """An overview of OBS Studio's Studio Mode can be found here: https://obsproject.com/wiki/OBS-Studio-Overview#studio-mode"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def streamreport(self,message,*,extra_text=""):
      factoid = """Interested to learn more about streaming settings, bitrates, encoder presets, and how they affect the quality of your stream? Check out a detailed report here: https://streamquality.report/docs/report.html"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def streamkey(self,message,*,extra_text=""):
      factoid = """A stream key is a unique string that is used to identify your account to a streaming service. You can usually find it in your profile settings for the service you're looking to stream to. Make sure not to share it with anyone! Twitch's stream key can be found in your dashboard, here: https://dashboard.twitch.tv/settings/stream"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def streamfx(self,message,*,extra_text=""):
      factoid = """If you are looking for more information or support for the StreamFX plugin, please visit the [forum resource page.](https://obsproject.com/forum/resources/streamfx-for-obs%C2%AE-studio.578/)"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def stalecookie(self,message,*,extra_text=""):
      factoid = """Exit OBS (make sure OBS is not running)
Delete the folder %appdata%\obs-studio\plugin_config\obs-browser\obs_profile_cookies
Start OBS
Settings -> Stream -> disconnect -> connect"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def srt(self,message,*,extra_text=""):
      factoid = """SRT is a streaming protocol, like RTMP: https://en.wikipedia.org/wiki/Secure_Reliable_Transport. In OBS Studio 25.0 and later, you can output via SRT to appropriate servers by going to Stream settings and selecting "Custom" for your service, then entering your srt:// path into the Server box. For a more complete guide on SRT and how to use it with OBS, see this article: https://obsproject.com/wiki/Streaming-With-SRT-Protocol"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def speedtest(self,message,*,extra_text=""):
      factoid = """Speed tests mean very little with regards to streaming and your choice of bitrate. They measure your raw upload speed to a server that's near you (likely run by your local ISP), instead of your stable upload speed to a streaming server. Your stable speed will determine the bitrate you can comfortably stream at.
The stable speed can be estimated as roughly 70-75% of the speed test result in a lot of cases, however this is by no means a perfect estimate. In reality, it may end up being much worse if there's problems between your ISP and the streaming service."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def sources(self,message,*,extra_text=""):
      factoid = """For a guide on the various sources and how they work in OBS Studio, see our guide here: https://obsproject.com/wiki/Sources-Guide"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def software(self,message,*,extra_text=""):
      factoid = """List of software for streaming and recording: https://helping-squad.com/useful-links/
List of software for editing: http://obsproject.com/forum/resources/234/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def sl(self,message,*,extra_text=""):
      factoid = """If you need advanced help with StreamLabs app or services, please join their [Discord server](https://discord.gg/xFcsxft) or submit a [support ticket.](https://support.streamlabs.com/hc/en-us/requests/new)"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def skype(self,message,*,extra_text=""):
      factoid = """The recommended way to capture a Skype call is using NDI. Guide: https://www.youtube.com/watch?v=SmmHln-2kZw
(Note: this does not work with 'Skype for Windows 10', only 'Skype for Windows', which also works on Windows 10)
As part of OBS Studio 25, you can now Window Capture Skype without disabling hardware acceleration.
Requirements:
Windows 10 Version 1903 or newer (open winver.exe to check)
Window Capture "Capture Method": 'Windows Graphics Capture'"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def simple(self,message,*,extra_text=""):
      factoid = """Advanced output mode, while allowing for more fine-tuning of options, does not automatically mean that your stream or recording will have better quality. Often, it can result in lower quality, because it can allow changes to settings that really shouldn't be changed. In most cases, Simple output mode is the best option to get the most out of OBS.
To change back to Simple output mode:
1) Go to Settings > Output in OBS.
2) Change "Output Mode" from "Advanced" to "Simple"."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def sidechain(self,message,*,extra_text=""):
      factoid = """Sidechain compression (ducking) is available by using the Compressor filter on your audio sources. For a video guide, see: https://www.youtube.com/watch?v=1Te2JERlInQ"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def shortcuts(self,message,*,extra_text=""):
      factoid = """A list of the pre-defined shortcuts in OBS can be found here: [Keyboard Shortcuts List](https://obsproject.com/wiki/Keyboard-Shortcuts)"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def settings(self,message,*,extra_text=""):
      factoid = """OBS Studio's settings can be found in the following OS specific locations:
Windows: WinKey+R > %APPDATA%\obs-studio
macOS: Cmd+Shift+G > ~/Library/Application Support/obs-studio
Linux: ~/.config/obs-studio"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def sehelp(self,message,*,extra_text=""):
      factoid = """If you need advanced help with StreamElements plugins or services, please join their [Discord server](https://discordapp.com/invite/se) or submit a [support ticket.](https://support.streamelements.com/hc/en-us/requests/new)"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def se(self,message,*,extra_text=""):
      factoid = """To cleanly remove the OBS.live plugin:
Uninstall OBS.Live
Uninstall OBS Studio (make sure that "User Settings" is not selected)
Install OBS Studio again from https://obsproject.com/
Your settings will be saved unless you have selected to delete them during removal."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def scripts(self,message,*,extra_text=""):
      factoid = """Scripts for OBS can be found here: https://obsproject.com/forum/resources/categories/5/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def scripting(self,message,*,extra_text=""):
      factoid = """A guide for getting started with development for scripting in OBS can be found on the wiki.
Additionally, you can find documentation for the scripting API here."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def screenshot(self,message,*,extra_text=""):
      factoid = """How to take a screenshot - http://www.take-a-screenshot.org/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def sceneswitcher(self,message,*,extra_text=""):
      factoid = """An advanced scene switcher plugin, with options for timed switching, cursor detecting, and further automation options, is available for OBS Studio on Windows, macOS, and Linux. Download links and installation instructions can be found here: http://obsproject.com/forum/resources/395/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def savage(self,message,*,extra_text=""):
      factoid = """I reject your reality and substitute my own!"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def requirements(self,message,*,extra_text=""):
      factoid = """OBS Studio requires a DirectX 10.1 (Windows) or OpenGL 3.3 (Mac, Linux) compatible video card (GPU).
The CPU requirements vary considerably depending on the chosen encoder, resolution, FPS and your scene complexity.
Try the Auto Configuration Wizard to find appropriate settings for your specs. See: https://obsproject.com/wiki/System-Requirements"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def replaybuffer(self,message,*,extra_text=""):
      factoid = """The replay buffer is a feature that allows you to keep a rolling buffer of OBS' output for a set amount of time (known as "flashback recording"), which can be saved to disk as a recorded video when a hotkey is pressed. You can enable it via Settings -> Output."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def remux(self,message,*,extra_text=""):
      factoid = """Remuxing allows you to take one video container (FLV, MKV, etc) and make an exact copy of the video and audio in another video container. This process takes seconds, and can be done with any recordings made with OBS by selecting File > Remux Recordings.
Remuxing is the safest way to get MP4 files for use in editors, or other software which doesn't support FLV or MKV files."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def remotedebugging(self,message,*,extra_text=""):
      factoid = """To expose Chrome Dev Tools for your browser sources, add --remote-debugging-port=1234 to your OBS Studio shortcut (where 1234 is your preferred port number) and navigate to http://localhost:1234/ in Chrome to connect to the session"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def remote(self,message,*,extra_text=""):
      factoid = """If you'd like to control OBS Studio remotely, you have a few options.
To control from the web on any device (including phones and computers), use OBS Tablet Remote (requires obs-websocket).
If you'd prefer a mobile app that works like the Elgato Streamdeck, you can try Touch Portal, UP Deck, or Deckboard."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def refresh(self,message,*,extra_text=""):
      factoid = """Due to Windows' limitations, using multiple displays with different refresh rates will cause performance issues in hardware-accelerated applications, including OBS. You can fix this by setting all displays to the same refresh rate. An easier solution may be to simply use monitors that all have the same refresh rate.
This problem is fixed in the Windows 10 May 2020 Update, which has started rolling out to users as of May 27, 2020."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def recursion(self,message,*,extra_text=""):
      factoid = """!recursion"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def recordings(self,message,*,extra_text=""):
      factoid = """OBS Studio recordings can be found by selecting File > Show Recordings. The output path can be changed under Settings > Output."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def rc(self,message,*,extra_text=""):
      factoid = """Details about the latest OBS Studio 27 release candidate can be found here: https://obsproject.com/forum/threads/obs-studio-27-release-candidate.141857/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def r6(self,message,*,extra_text=""):
      factoid = """Rainbow Six: Siege Vulkan can now be captured with OBS 25 RC5 or higher. Keep in mind that OBS might need to run as administrator to capture the game successfully."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def quicksync(self,message,*,extra_text=""):
      factoid = """If the Quick Sync option in OBS is unavailable, read http://obsproject.com/forum/resources/82/
Note that hardware encoders like Quick Sync will produce lower quality compared to x264 at the same bitrate, and are best suited for local recordings rather than streaming."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def quality(self,message,*,extra_text=""):
      factoid = """Interested in learning more about how video compression and streaming/recording quality work? Watch http://www.youtube.com/watch?v=r6Rp-uo6HmI"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def protectedfolders(self,message,*,extra_text=""):
      factoid = """The Windows Controlled Folder Access setting can prevent OBS from being able to record to your PC. It is recommended that you disable it.
Click on start and search for Windows Defender Security Center
Click on Virus & threat protection
Click the Virus & threat protection settings option
Turn off the Controlled folder access toggle switch"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def programcapture(self,message,*,extra_text=""):
      factoid = """Unfortunately, it is impossible to capture only a single program's audio in Windows due to limitations of the Windows API. Windows only makes it possible to capture all audio from a specific device. Instead, try creating a virtual audio device using something like Virtual Audio Cable or Voicemeeter Banana, and set your programs to output to that device."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def pride(self,message,*,extra_text=""):
      factoid = """Wondering what the logo on the Alpha Gaming server is? It's the LGBTQ+ Pride flag, showing our support for Pride Month! For more information, [click here](https://www.loc.gov/lgbt-pride-month/about/)"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def portablevc(self,message,*,extra_text=""):
      factoid = """To install the OBS virtual camera when running OBS in portable mode, navigate to your <your obs-studio folder>\data\obs-plugins\win-dshow and run virtualcam-install.bat as Administrator."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def portable(self,message,*,extra_text=""):
      factoid = """Portable Mode allows the program to save and access configuration data from the program's base folder. To enable portable mode:
1.) Install/unzip to a custom directory outside of "C:\Program Files (x86)" or "C:\Program Files"
2.) Then either modify its shortcut with the --portable or -p command line parameter, or create a blank text file named "portable_mode.txt" in the base installation/unzip folder."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def plugintemplate(self,message,*,extra_text=""):
      factoid = """A template for new OBS plugins including boilerplate code and CI scripts can be found at https://github.com/obsproject/obs-plugintemplate"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def plugins(self,message,*,extra_text=""):
      factoid = """How to install plugins: https://obsproject.com/forum/resources/421/
List of available plugins: https://obsproject.com/forum/resources/categories/6/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def periscope(self,message,*,extra_text=""):
      factoid = """The community has created a guide for streaming to Periscope with OBS: https://obsproject.com/forum/resources/508/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def pause(self,message,*,extra_text=""):
      factoid = """To enable "Pause Recordings", do the following:
In Settings -> Output, make sure "Recording quality" is not set to "Same as stream". If you are using advanced output, make sure that the encoder is not set to "(Use stream encoder)".
If you want, set a Pause hotkey in Settings -> Hotkeys
Start Recording. While recording, you should see a ⏸ icon next to the Stop Recording button."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def patreon(self,message,*,extra_text=""):
      factoid = """OBS is on Patreon! Support Jim, the project's lead developer, as he works full time on OBS: https://www.patreon.com/obsproject"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def partial(self,message,*,extra_text=""):
      factoid = """Most video editing applications and video streaming platforms expect a Partial-range input; streaming or recording in Full range will result in color clipping, often reported as overly bright or dark image. You can change your color range setting in Settings > Advanced."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def params(self,message,*,extra_text=""):
      factoid = """For a list of launch parameters, see: https://obsproject.com/wiki/Launch-Parameters"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def opengl(self,message,*,extra_text=""):
      factoid = """Please type 'glxinfo | grep OpenGL' into your terminal, upload the output to a site like http://pastebin.com/ and then link it here."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def oc(self,message,*,extra_text=""):
      factoid = """You can sponsor OBS development through Open Collective, a platform for funding groups will full transparency: https://opencollective.com/obsproject"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def nvafx(self,message,*,extra_text=""):
      factoid = """The redistributables required for the NVIDIA Noise Removal filter can be found here: https://www.nvidia.com/en-us/geforce/broadcasting/broadcast-sdk/resources/
Once installed, the NVIDIA Noise Removal option will appear as part of the "Noise Suppression" filter, alongside RNNoise and Speex."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def nginx(self,message,*,extra_text=""):
      factoid = """Setting up your own nginx RTMP server (Linux-based guide): http://obsproject.com/forum/threads/12891/
Pre-built nginx Windows binaries: https://github.com/illuspas/nginx-rtmp-win32"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def newscenecollection(self,message,*,extra_text=""):
      factoid = """Please create a new Scene Collection for testing purposes. Use the Scene Collection menu at the top of OBS, select New, and call it "Testing". Then, add your sources that are suspected to have issues."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def new(self,message,*,extra_text=""):
      factoid = """New to OBS? [Check out our 4 step quickstart guide.](https://obsproject.com/wiki/OBS-Studio-Quickstart)
Want to learn even more? Check out our [in-depth overview.](https://obsproject.com/wiki/OBS-Studio-Overview)
If you'd prefer to learn with videos, check out these guides made by the community:
[Nerd or Die's quickstart video guide](https://youtube.com/watch?v=5rlrDIwnGGQ&t=0s&list=PLT3Ure7_kYHwj8oT3AV-pZ4_r7yp6mDg-)
[EposVox's OBS Master Class](https://youtube.com/watch?v=nK-Mu7nw5EA&list=PLzo7l8HTJNK-IKzM_zDicTd2u20Ab2pAl)"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def nditools(self,message,*,extra_text=""):
      factoid = """NDI Tools can be downloaded here:
Windows
Windows Analysis Tool
Mac"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def ndisdk(self,message,*,extra_text=""):
      factoid = """The NDI SDK can be found here: http://pages.newtek.com/NDI-Developers-SDK-Download-Link.html"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def ndi(self,message,*,extra_text=""):
      factoid = """OBS Studio has an NDI plugin available, which can be found here: https://obsproject.com/forum/resources/528/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def multirtmp(self,message,*,extra_text=""):
      factoid = """A third party plug-in for streaming to multiple RTMP servers is available for OBS Studio. https://obsproject.com/forum/resources/multiple-rtmp-outputs-plugin.964"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def mp4(self,message,*,extra_text=""):
      factoid = """Record to FLV or MKV. If you record to MP4 and the recording is interrupted, the file will be corrupted and unrecoverable. If you require MP4 files for some other purpose like editing, remux them afterwards by selecting File > Remux Recordings in the main OBS Studio window."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def mojave(self,message,*,extra_text=""):
      factoid = """As of macOS 10.14 (Mojave), SyphonInject will no longer work on macOS, which means that Game Capture cannot be used. Game Capture on macOS relied on SyphonInject to work at all. Use a Window Capture or Display Capture instead of your Game Capture. We apologize for the inconvenience."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def mobile(self,message,*,extra_text=""):
      factoid = """OBS will not be developed for mobile devices. Mobile hardware is typically too weak to do what OBS does, and mobile development is currently outside the scope of what the project can work on right now. If all you're looking for is a way to control OBS through your phone, please type !remote."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def mixer(self,message,*,extra_text=""):
      factoid = """Curious what all the extra information in OBS' volume meters is? Check out our guide here: https://obsproject.com/wiki/Understanding-The-Mixer"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def mic(self,message,*,extra_text=""):
      factoid = """To filter out background noise, use the Noise Suppression filter which is included in OBS Studio 26.0.0+"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def memes(self,message,*,extra_text=""):
      factoid = """No."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def media(self,message,*,extra_text=""):
      factoid = """Curious what video formats are the most performant in OBS?
Check out [EposVox's in-depth analysis!](https://www.youtube.com/watch?v=X9jMna8KQyA&feature=youtu.be)"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def manualpastebin(self,message,*,extra_text=""):
      factoid = """Go to:
Windows: `%APPDATA%\obs-studio\logs`
Linux: `~/.config/obs-studio/logs`
Mac: `~/Library/Application Support/obs-studio/logs`
Then copy the contents of the desired log (usually the latest) file to https://pastebin.com/. Save the file on Pastebin at the bottom of the window, then copy the new URL and paste it here."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def manuallog(self,message,*,extra_text=""):
      factoid = """Please manually upload your log file.
(Windows)
Press `WinKey+R` to open the Run dialog
Paste the following into the box and hit OK: `%APPDATA%\obs-studio\logs`
Find the desired log file (usually the latest) and drag/drop it into this channel.
Linux logs: `~/.config/obs-studio/logs`
macOS logs: `~/Library/Application Support/obs-studio/logs`"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def manualcrash(self,message,*,extra_text=""):
      factoid = """To find the OBS Studio crash logs, follow these steps:
Press `WinKey+R` to open the Run dialog
Type in: `%APPDATA%\obs-studio\crashes` and press Enter
Upload the desired crash log, usually the latest, directly to this Discord channel by dragging and dropping the file into the chat window"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def manualcam(self,message,*,extra_text=""):
      factoid = """If your video capture device is not displaying video in OBS, try setting the resolution and FPS to something known that the device supports. Go to the Video Capture Device properties, change Resolution/FPS Type from Device Default to Custom, and then set the options accordingly."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def mantis(self,message,*,extra_text=""):
      factoid = """http://obsproject.com/mantis/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def macpermission(self,message,*,extra_text=""):
      factoid = """Please ensure OBS has permissions to access your microphone & capture devices.
1) Select System Preferences from the Apple menu.
2) Click the icon labelled Security & Privacy.
3) Click the Privacy tab at the top.
4) In the lefthand column, click on 'Microphone', 'Camera', 'Screen recording' or 'Accessibility' to manage app permissions.
5) Tick the box for OBS"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def macndi(self,message,*,extra_text=""):
      factoid = """Close OBS
Manually update obs-ndi via this link
Run this script
Try running OBS again"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def macminimum(self,message,*,extra_text=""):
      factoid = """OBS Studio 25+ requires macOS 10.13+."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def maclogi(self,message,*,extra_text=""):
      factoid = """https://i.imgur.com/wxwjVdr.png"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def macdocks(self,message,*,extra_text=""):
      factoid = """Custom browser docks and service integrations will be available in OBS Studio v27 for macOS and the Ubuntu PPA."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def maccrash(self,message,*,extra_text=""):
      factoid = """A crash log is required to investigate the cause of your issue. Please upload the most recent crash log.
In Finder, click the Go menu
Select Go To Folder, and type in ~/Library/Logs/DiagnosticReports/
Upload the file prefixed obs_ with the most recent date (format is year-month-day)"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def maccapture(self,message,*,extra_text=""):
      factoid = """Due to limitations from Apple, there is no Game Capture source available on macOS 10.14+. It is recommended that you use Display or Window Capture sources instead."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def macaudio(self,message,*,extra_text=""):
      factoid = """OBS Studio for macOS requires a second program to help it capture desktop audio, due to Apple not providing direct audio capture functionality
Click here for a guide using [BlackHole](https://obsproject.com/forum/resources/1191/)"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def mac(self,message,*,extra_text=""):
      factoid = """Releases of OBS for Mac can be found at http://obsproject.com/download (click the Apple!)
If you have any issues, please check the forum threads at https://obsproject.com/forum/list/33/
You must be on macOS 10.13 or later. You can update to version 10.13 of macOS (free!) http://www.apple.com/macos/how-to-upgrade/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def m1ndi(self,message,*,extra_text=""):
      factoid = """1) Close OBS
2) Download and install Newtek NDI®️ Studio Monitor and the OBS NDI®️ plugin
3) Open the Terminal app (you can find it in launchpad, comes pre-installed with every Mac)
4) Paste the following command into the terminal
sudo cp "/Applications/NewTek NDI Video Monitor.app/Contents/Frameworks/libndi.4.dylib" /usr/local/lib/libndi.4.dylib
5) Input your password (note: you will not see the password being put in, but it will be working)
6) Open OBS and check if NDI appears in the Tools menu"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def lol(self,message,*,extra_text=""):
      factoid = """To best capture League of Legends, create two scenes.
In the first scene, add a Window Capture of the LoL launcher/lobby (Windows 7 users should make sure Aero is enabled.).
In the second scene, add a Game Capture of the game itself (you may need to be in a game to add this for the first time).
Then configure the Scene Switcher to automatically swap between them."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def logo(self,message,*,extra_text=""):
      factoid = """High-quality versions of the OBS logo can be found here:
https://h4ndy.eu/seafile/d/ecaab7abeee84c4aabf1/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def logfolder(self,message,*,extra_text=""):
      factoid = """To see all of your logs, select Help > Log Files > Show Log Files.
If you want to manually analyse a log, upload it's contents to a service like Hastebin and use this tool."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def loganalyzer(self,message,*,extra_text=""):
      factoid = """To analyze an OBS log, you can use this online tool: https://obsproject.com/tools/analyzer"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def localadvanced(self,message,*,extra_text=""):
      factoid = """For an advanced guide to local recording settings, see: http://obsproject.com/forum/resources/221/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def local(self,message,*,extra_text=""):
      factoid = """For high-quality, no fuss recordings, use the recording quality presets.
1) Under Settings > Output, set the mode to Simple output.
2) In the recording section, change the Recording Quality to Indistinguishable Quality
3) Select your encoder. We recommend a hardware encoder if it is available."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def linux(self,message,*,extra_text=""):
      factoid = """http://obsproject.com/download#linux"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def lastlog(self,message,*,extra_text=""):
      factoid = """A log file is required to help fix your issue. Please post a link to your last log file.
In OBS select Help > Log Files > Upload Last Log File.
Copy the URL and paste it here.
(Note: If you do not see an obsproject.com URL, you will need to update OBS Studio to version 22+)"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def kraken(self,message,*,extra_text=""):
      factoid = """Problems getting the Razer Kraken working? Make sure you're using the 64-bit version of OBS. If you're stuck on a 32-bit system or the 64bit OBS still doesn't work, try disabling the Kraken launcher in msconfig's Startup tab (press WinKey+R, type "msconfig" in the box and press Enter) and reboot your pc."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def killernic(self,message,*,extra_text=""):
      factoid = """Killer's Firewall is known for its poor performance and issues when trying to stream. Please download the driver only package from http://support.killernetworking.com/software/, completely uninstall all Killer NIC items and install their Driver only package."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def slimport(self,message,*,extra_text=""):
      factoid = """As of OBS Studio 25, you can import Scene Collections from other applications, including OBS Classic, XSplit, and Streamlabs.
In OBS Studio, open the "Scene Collection" menu along the top
Choose "Import"
If asked to "Automatically Search for Scene Collections", choose "Yes" ^
Use the checkboxes ✅ on the left to choose what to import
Press "Import" along the bottom
Switch to the newly imported Collection via the "Scene Collection" menu
^ If the dialog did not appear, or you previously selected "No", go to Settings -> General -> Importers and enable 'Search known locations.''"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def hugh(self,message,*,extra_text=""):
      factoid = """https://clips.twitch.tv/OriginalEmpathicGoldfishBlargNaut"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def howtoinstall(self,message,*,extra_text=""):
      factoid = """Instructions on how to install or build OBS Studio can be found here:
https://obsproject.com/wiki/Install-Instructions"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def hotkeymode(self,message,*,extra_text=""):
      factoid = """Game capture sources allow you to use a hotkey mode to capture the currently active window, allowing you to use one game capture source for all of your games and even allowing you to switch games easily. To activate this mode:
Open the game capture source's properties. (You can do this by double clicking on the source in the sources list)
Change the game capture's Mode to "Capture foreground window with hotkey"
In Settings > Hotkeys, set up a hotkey for "Capture foreground window"."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def hi(self,message,*,extra_text=""):
      factoid = """Welcome to the Alpha Gaming community support channel. If you have a question, go ahead and ask it, and if someone is available to help they'll respond. Try to be as detailed as possible. Please be patient if someone doesn't respond right away!"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def hfr(self,message,*,extra_text=""):
      factoid = """To record framerates higher than 60fps, you will need very powerful hardware (SSD, high-end GPU, significant CPU overhead, fast RAM) in order to accomplish it. There are no simple instructions that will make it work. It is recommended that you stay at or under 120fps when using OBS, and we may be unable to provide support for higher framerates if your hardware cannot handle it. Be prepared for hours of trial and error on your own."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def hags(self,message,*,extra_text=""):
      factoid = """In Windows, go to ⚙️ Settings → System → Display → Graphics Settings.
Turn "Hardware-accelerated GPU scheduling" to OFF, then reboot your computer."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def greenscreen(self,message,*,extra_text=""):
      factoid = """For an in-depth overview of greenscreens and how they work, and how you can improve your own, check out this video: https://www.youtube.com/watch?v=OH8TWTt51W8"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def gpuz(self,message,*,extra_text=""):
      factoid = """Please download GPU-Z and post a screenshot of the Graphics Card tab. Click the 📷 button in the upper right and select Upload to Free Image Hosting, then post the link here.
Download link: https://www.techpowerup.com/download/techpowerup-gpu-z/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def gpun(self,message,*,extra_text=""):
      factoid = """You need to update your NVIDIA drivers. You have 2 ways you can do it:
Open GeForce Experience if it's installed on your PC. Login, click on DRIVERS, then select Download. Install it fully, then reboot.
OR
Manually download your drivers using this link: https://www.geforce.com/drivers
Make sure to reboot your PC once the drivers are installed."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def gpui(self,message,*,extra_text=""):
      factoid = """You need to update your Intel video driver. You have 2 ways you can do this:
Update using the Intel Driver & Support Assistant, available at this link: https://www.intel.com/content/www/us/en/support/detect.html
Update by selecting the appropriate driver for your OS and GPU, at this link: https://downloadcenter.intel.com/product/80939/Graphics-Drivers
Always reboot your PC once your drivers are updated, even if you are not prompted to."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def gpudriver(self,message,*,extra_text=""):
      factoid = """You can perform a clean driver installation for your GPU by following the instructions at http://obsproject.com/forum/resources/65/.
Using an AMD GPU? Use the AMD Cleanup Utility instead. https://www.amd.com/en/support/kb/faq/gpu-601"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def gpuconnection(self,message,*,extra_text=""):
      factoid = """https://i.imgur.com/3Z5RETY.png"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def gpua(self,message,*,extra_text=""):
      factoid = """You need to update your AMD video driver. You have 2 ways you can do this:
Update using the AMD Driver Auto-Detect Tool, available at this link: https://www.amd.com/en/support/kb/faq/gpu-131
Update by selecting your specific video card type at this link: https://www.amd.com/en/support
Always reboot your PC once your drivers are updated, even if you are not prompted to."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def gpl(self,message,*,extra_text=""):
      factoid = """The source code for OBS Studio is released under the GPLv2 license. Effectively, that means that anyone can read, use, or modify the code for their own purposes, but if they distribute a program using that modified code, they must also make the source code available to whoever uses that program."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def git(self,message,*,extra_text=""):
      factoid = """The GitHub repository for OBS Studio can be found here: obsproject/obs-studio
The repository for the bot itself can be found here: obsproject/obs-bot"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def gamedvr(self,message,*,extra_text=""):
      factoid = """To ensure that OBS Studio has the hardware resources it needs for realtime streaming and recording, we recommend disabling the "Game DVR Background Recording" feature via these instructions: https://obsproject.com/wiki/How-to-disable-Windows-10-Gaming-Features#game-dvrcaptures"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def gamecapture(self,message,*,extra_text=""):
      factoid = """For a starting guide on game capture and its modes, please read [this guide](https://obsproject.com/wiki/Game-Capture-Guide).
If Game Capture isn't working properly for you and your games, make sure to read this [guide for common solutions](https://obsproject.com/wiki/Game-Capture-Guide#common-resolutions-for-game-capture-issues)."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def fullscreen(self,message,*,extra_text=""):
      factoid = """If a game is set to run in full-screen mode, when you alt+tab out the game, it will stop rendering. This means that you will not see the game in OBS while it is minimized. Either make a test recording and check it to verify the capture worked properly, or move OBS to a second monitor if you have one."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def free(self,message,*,extra_text=""):
      factoid = """OBS Studio is completely, 100% free. You don't have to pay for it at all. It is a great, high quality program that excels at both streaming and recording. OBS Studio is guaranteed to be completely virus and malware free, as long as you download them from the official website at https://obsproject.com/download"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def fpslimit(self,message,*,extra_text=""):
      factoid = """Running a game without vertical sync or a frame rate limiter will frequently cause performance issues (both your game and OBS) because your GPU will be maxed out. Enable vsync or set a reasonable frame rate limit that your GPU can handle without hitting 100% usage. If that's not enough you may also need to turn down some of the video quality options in the game.
For more technical details and alternate fixes, see our guide: https://obsproject.com/wiki/GPU-overload-issues"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def flash(self,message,*,extra_text=""):
      factoid = """Old versions of Flash player installed on your system may cause OBS or the browser source to crash on startup. Please run the Flash uninstaller from https://obsproject.com/downloads/uninstall_flash_player.exe"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def firefox(self,message,*,extra_text=""):
      factoid = """Having trouble window capturing Firefox? You may need to disable hardware acceleration for window capture to work properly. Follow these steps to disable it:
Open your Firefox Options.
In the Find in options box, type in hardware.
Uncheck both Use recommended performance settings and Use hardware acceleration when available.
Restart Firefox
Note: Disabling hardware acceleration can cause performance loss on certain web pages."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def filters(self,message,*,extra_text=""):
      factoid = """Many options for fine-tuning your video and audio sources in OBS Studio are in the Filters menu. To access this menu, right click on your source (or click the Gear icon next to an audio source) and select Filters.
For more info, see our guide: https://obsproject.com/wiki/Filters-Guide"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def fider(self,message,*,extra_text=""):
      factoid = """Have an idea for OBS Studio? Let us know! https://ideas.obsproject.com/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def facebookbitrate(self,message,*,extra_text=""):
      factoid = """You can find Facebook's recommended bitrates for different resolutions here: https://www.facebook.com/fbgaminghome/creators/best-practices#streamSettings
However, our general recommendations are:
1080p60 - 6 Mbps
1080p30 - 6 Mbps
720p60 - 6 Mbps
720p30 - 3-4 Mbps, depending on the game"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def facebook(self,message,*,extra_text=""):
      factoid = """A guide for streaming to Facebook is available at http://obsproject.com/forum/resources/391/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def export(self,message,*,extra_text=""):
      factoid = """To export OBS settings to back them up, go to Profile > Export (to export streaming/recording settings) and Scene Collection > Export (to export scenes)."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def exclusive(self,message,*,extra_text=""):
      factoid = """To disable Exclusive Mode:
1) Right-click the speaker icon in the System Tray and select "Sounds".
2) In the "Playback" or "Recording" tabs, right click on the audio device(s) you want to change and select "Properties".
3) Then go to the "Advanced" tab and uncheck both checkboxes."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def error(self,message,*,extra_text=""):
      factoid = """Please provide the full text of the error message. Press Alt+PrtScr while the error window is selected to copy it to your clipboard, then paste it into this chat window."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def elgatosupport(self,message,*,extra_text=""):
      factoid = """For help with Elgato products, please submit a ticket with them directly at https://help.elgato.com/hc/en-us/requests/new. They also have a community Discord server."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def elgatomac(self,message,*,extra_text=""):
      factoid = """Elgato doesn't provide macOS drivers for the HD, HD60, or HD60 S that work with OBS, so they can't be added as a Video Capture device. For these cards you'll have to capture Elgato's software running in fullscreen via Window Capture.
However, Elgato now has OBS Link as a new NDI-based workaround tool for the HD 60 S to add OBS compatibility.
For native macOS support via UVC, please consider the Elgato Cam Link or HD60 S+ ("plus")."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def elgatodrivers(self,message,*,extra_text=""):
      factoid = """In many cases, installing only the driver packages for Elgato Game Capture cards works better with OBS than installing the full software suite. Links can be found here: https://help.elgato.com/hc/en-us/articles/360027961152-Elgato-Gaming-Hardware-Drivers"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def elgatocrash(self,message,*,extra_text=""):
      factoid = """If OBS is crashing due to Elgato's drivers, follow these steps (carefully, in order!) to correct it.
1) Unplug your Elgato device (if USB)
2) Uninstall all Elgato software and drivers from Add/Remove Programs
3) Reboot your PC (Very important you do this before trying to install anything else)
4) Reinstall the Elgato software/drivers
5) Plug the Elgato card back in (if not already prompted to during the Elgato software installation)"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def electron(self,message,*,extra_text=""):
      factoid = """In order to capture most electron applications using window capture you have to disable hardware acceleration first."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def editor(self,message,*,extra_text=""):
      factoid = """Editor functionality is not something that is currently in scope for OBS development at this time. While editing features would be nice, the main focus on development in OBS right now is on improving OBS's streaming and recording features, and we're happy to leave the editing step for other, more specialized programs to handle. Here is a good list of editing software that we recommend you check out: https://obsproject.com/wiki/Post-Production-Tools-You-Can-Use"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def echo(self,message,*,extra_text=""):
      factoid = """To avoid audio feedback or echo, don't watch your own stream on the same computer you are streaming from. If you have already ruled this out as a possible issue, please post a log. Help → Log Files → Upload Current Log. Copy the URL and paste it here."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def dynamicbitrate(self,message,*,extra_text=""):
      factoid = """You can enable Dynamic Bitrate in Settings -> Advanced -> Network -> "Dynamically change bitrate to manage congestion (Beta)"
When enabled, instead of dropping frames when you have network issues, OBS will automatically reduce your stream quality to compensate. OBS will adjust back to normal once your connection becomes stable."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def dx12(self,message,*,extra_text=""):
      factoid = """There is a known issue when using game capture to capture DirectX 12 games where frames may be returned out of order, causing a stuttering effect. We are working on ways to deal with the issue, but it will be some time before a proper fix or workaround is available. For the time being, the best solution would be to lock your game to 60FPS and change the Hook Rate setting in your game capture source to "Fastest". Otherwise, consider trying display capture instead of game capture."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def dump(self,message,*,extra_text=""):
      factoid = """Please create a memory dump file, so that we can look at the problem more closely: https://obsproject.com/forum/resources/598/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def ducking(self,message,*,extra_text=""):
      factoid = """If you're experiencing sound volume reduction when OBS is opened, try checking the "Disable Windows audio ducking" option in Settings > Audio > Advanced, in OBS. Then restart OBS to see if the issue is resolved."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def dslr(self,message,*,extra_text=""):
      factoid = """DSLR cameras and camcorders are not built to be webcams. Preview functions via USB can't be used in OBS. To get a clean video and audio feed from a DSLR or camcorder, you need a HDMI capture card. Lastly, note that a high quality webcam is often cheaper than a capture card."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def droste(self,message,*,extra_text=""):
      factoid = """What you are seeing is normal and is called the Video Feedback Effect. It will go away when you stop looking at the OBS preview on the same display you're capturing. Read https://en.wikipedia.org/wiki/Video_feedback for more info."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def driveby(self,message,*,extra_text=""):
      factoid = """https://twitter.com/cassidoo/status/1294077384128212992"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def dpi(self,message,*,extra_text=""):
      factoid = """Due to issues with how Qt handles high-DPI display scaling, you may encounter some oddities in the OBS Studio UI when using DPI scaling. As a workaround, you can disabled DPI scaling for OBS:
Close OBS Studio.
Find your OBS Studio shortcut, either on your desktop or in your start menu (Right click -> Open file location).
Right click on it and select "Properties".
Go to the "Compatibility tab".
Click "Change high DPI settings".
Tick "Override high DPI scaling behavior".
In the dropdown, change it to "System (Enhanced)".
Click OK to exit out of the scaling settings.
Click OK to save the new properties.
Launch OBS Studio as you normally would."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def downtime(self,message,*,extra_text=""):
      factoid = """The Fastly CDN currently has local connectivity issues. This affects multiple sites, including Twitch.tv, Reddit, Amazon, Github, as well as our own OBS Project website and downloads. Service should hopefully be restored shortly."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def download(self,message,*,extra_text=""):
      factoid = """OBS Studio can be downloaded right from the OBS Project website: https://obsproject.com/download"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def downgrade(self,message,*,extra_text=""):
      factoid = """Need an older version of OBS? Go to https://github.com/obsproject/obs-studio/releases for OBS Studio versions back to 0.2.4"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def donate(self,message,*,extra_text=""):
      factoid = """You can support OBS development by either becoming a patron on the OBS Patreon or by becoming a sponsor on the OBS Open Collective.
Find out more here: https://obsproject.com/contribute"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def docs(self,message,*,extra_text=""):
      factoid = """Developer documentation for OBS can be found here: https://obsproject.com/docs/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def docks(self,message,*,extra_text=""):
      factoid = """You can manage your docks from the View > Docks menu.
You can toggle docks on and off, or lock or unlock docks to prevent moving and editing.
You can also reset the UI from this menu to return your docks to their original state (View > Docks > Reset UI)."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def docki(self,message,*,extra_text=""):
      factoid = """https://i.imgur.com/YANZ4RG.png """
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def directx(self,message,*,extra_text=""):
      factoid = """Missing DirectX components? Download the DirectX Web Installer from http://obsproject.com/go/dxwebsetup
If the web installer won't work, try the DirectX Dependency Fixer from http://obsproject.com/forum/resources/87/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def diagnostic(self,message,*,extra_text=""):
      factoid = """Please run the OBS Diagnostics Tool to determine if there are any issues with system files that support OBS: https://obsproject.com/downloads/OBSDiag.zip
Once the tool has been run, screenshot the output (click the window and press the alt+printscreen keys on your keyboard) and post the screenshot (ctrl+v) here."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def destiny2(self,message,*,extra_text=""):
      factoid = """Bungie has opted to not allow OBS to hook Destiny 2 using Game Capture. See: https://www.bungie.net/en/Help/Article/46101
You will need to run the game in either windowed fullscreen or borderless windowed and use Window Capture instead."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def deps(self,message,*,extra_text=""):
      factoid = """Pre-built dependencies: VS2019
CEF for browser source/panels: x86, x64
Qt 5.15.2: Windows, macOS"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def dell(self,message,*,extra_text=""):
      factoid = """The Dell Backup and Recovery tool has a component that will cause issues with OBS, resulting in a crash. You can correct it by either uninstalling the tool completely if it is not being used, or by running this file as administrator on the system: https://obsproject.com/downloads/UnregisterDellBackup.cmd"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def delay(self,message,*,extra_text=""):
      factoid = """If you need to delay your audio sources, go to Edit -> Advanced Audio Properties and adjust the Sync Offset (ms) field. If you need to delay your video sources, add a Video Delay (Async) filter. For other sources (Window/Game/Display Capture), add a Render Delay filter and adjust as necessary."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def cyberpunk2077(self,message,*,extra_text=""):
      factoid = """Cyberpunk 2077 is a very resource-intensive game. Additionally, it's also a DirectX 12 game, which means it can have issues with frame pacing.
To minimize the game's impact on OBS performance, limit the game to a stable frame rate (e.g. 60 FPS) and consider turning down your graphics quality settings."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def csgo(self,message,*,extra_text=""):
      factoid = """Valve has implemented a Trusted mode which does not allow OBS to hook CS:GO using Game Capture. Read more in their announcement post. Additionally, they have no plans on allowing OBS in Trusted mode.
We recommend running the game in either windowed or borderless fullscreen and using a Window Capture source instead.
Alternately, you can launch the game with -allow_third_party_software ."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def crowdin(self,message,*,extra_text=""):
      factoid = """To help with the translation of OBS see: http://crowdin.com/project/obs-studio"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def crop(self,message,*,extra_text=""):
      factoid = """To crop sources in OBS Studio, first reset the source to its default size by clicking on it and pressing ctrl+r. Then hold the alt key and drag the red box around the source you wish to crop. The sides will turn green to indicate they are cropped. Note that the preview must be unlocked in order to do this."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def crashlog(self,message,*,extra_text=""):
      factoid = """A crash log is required to investigate the cause of your issue. Please upload the last crash log.
In OBS, click the Help menu
Select Crash Reports, and then Upload Last Crash Report
Copy the URL, and paste it to the chat here."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def cpu(self,message,*,extra_text=""):
      factoid = """Having issues with high CPU usage, or getting a warning about "Encoding overloaded!"? Read https://obsproject.com/wiki/General-Performance-and-Encoding-Issues"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def coreaudio(self,message,*,extra_text=""):
      factoid = """You can install Apple's CoreAudio codecs for better audio quality without bothering with iTunes or QuickTime. Follow the instructions at http://obsproject.com/forum/resources/220/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def converter(self,message,*,extra_text=""):
      factoid = """A tool for converting OBS Classic scenes to OBS Studio is available at http://obsproject.com/forum/resources/430/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def contributing(self,message,*,extra_text=""):
      factoid = """To get started with OBS development, read this guide."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def conflicts(self,message,*,extra_text=""):
      factoid = """Some third-party applications can conflict with OBS and cause issues, such as failing Game or Window capture, audio issues, and at worst crashes with OBS. For a full list, check here: https://obsproject.com/wiki/Known-Conflicts"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def cleanprofile(self,message,*,extra_text=""):
      factoid = """Please post a link to a clean log with profiler information. To make a clean log with profiler information, follow these steps:
1) Restart OBS.
2) Start your stream/recording for ~30 seconds, and stop it again. Make sure you replicate any issues as best you can, which means having any games/apps open and captured, etc.
3) Restart OBS again, and then select Help > Log Files > Upload Last Log File. Copy the URL and paste it here.
(Note: If you do not see an obsproject.com URL, you will need to update OBS Studio to version 22+.)"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def cleanlog(self,message,*,extra_text=""):
      factoid = """A clean log file is required to help fix your issue. To make a clean log file, please follow these steps:
1) Restart OBS
2) Start your stream/recording for at least 30 seconds (or however long it takes for the issue to happen). Make sure you replicate any issues as best you can, which means having any games/apps open and captured, etc.
3) Stop your stream/recording.
4) Select Help > Log Files > Upload Current Log File. Copy the URL and paste it here."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def classic(self,message,*,extra_text=""):
      factoid = """If you are still using OBS Classic, please note that this version is no longer supported. While we cannot and will not do anything to prevent you from using it, we cannot help with any issues that may come up. It is recommended that you update to OBS Studio. Further information on why you should update (and how): https://obsproject.com/forum/threads/55820/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def chromeos(self,message,*,extra_text=""):
      factoid = """OBS will not be developed for ChromeOS. The operating system has too many limits in place that prevent OBS from being able to do what it needs to do, and more often than not, Chromebook hardware is too weak to render and encode live video. The Linux Beta for ChromeOS does not change this."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def chrome(self,message,*,extra_text=""):
      factoid = """As part of OBS Studio 25, you can now Window Capture Google Chrome without disabling hardware acceleration.
Requirements:
Windows 10 Version 1903 or newer (open winver.exe to check)
Window Capture "Capture Method": "Windows Graphics Capture"
For older versions of Windows, do the following:
Open Chrome Settings.
In the Search settings box, type in hardware.
Ensure that the slider next to the Use hardware acceleration when available option is turned off.
Click Relaunch to restart Chrome."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def chatdocks(self,message,*,extra_text=""):
      factoid = """To enable Chat docks for Twitch or Restream, you will need to connect your account via Settings -> Stream.
If you'd like to enable chat docks for other services, you can use View -> Docks -> Custom Browser Docks. This allows you to include any webpage in OBS."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def changelog(self,message,*,extra_text=""):
      factoid = """Previous versions of OBS Studio can be found here: https://github.com/obsproject/obs-studio/releases"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def cert(self,message,*,extra_text=""):
      factoid = """Twitch is currently having an issue with a certificate provider, which is causing problems when fetching channel data and preventing people from connecting to their Twitch accounts. They are aware of the issue and are working on resolving it. In the meantime, you can still stream by disconnecting your Twitch account and entering your stream key from here: https://dashboard.twitch.tv/settings/channel"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def catalina(self,message,*,extra_text=""):
      factoid = """OBS 24.0.6 is out with many fixes, including Catalina support. Download it via the website https://obsproject.com/download"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def capturecards(self,message,*,extra_text=""):
      factoid = """Which capture card should I get for streaming or recording? And do I need one? (avoid USB 2.0 capture devices if at all possible) - http://www.helping-squad.com/which-capture-card-should-i-get-for-streaming-or-recording/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def camflip(self,message,*,extra_text=""):
      factoid = """The view you see in your application is flipped for you only. This is because most applications expect a webcam, and they want to mimic looking in a mirror for your own preview. Everyone else sees what you see in the OBS preview."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def camav(self,message,*,extra_text=""):
      factoid = """Many modern antivirus programs have added in and automatically enabled webcam protection features that block applications such as OBS from being able to access webcams and capture cards. Check that your antivirus program does not have a webcam/video device blocking feature, and if it does, you will need to add OBS as an exception."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def cam(self,message,*,extra_text=""):
      factoid = """Guides to getting the most out of your webcam:
http://obsproject.com/forum/threads/1036/
https://www.youtube.com/watch?v=6NY8wWo_VBs"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def cache(self,message,*,extra_text=""):
      factoid = """The OBS Browser cache can be found in the following locations:
Windows: %appdata%\obs-studio\plugin_config\obs-browser
macOS: ~/Library/Application Support/obs-studio/plugin_config/obs-browser
Linux: ~/.config/obs-studio/plugin_config/obs-browser"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def bye(self,message,*,extra_text=""):
      factoid = """Thank you, have a nice day, goodbye. o/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def buffering(self,message,*,extra_text=""):
      factoid = """Is a stream buffering for you or some of your viewers? Read https://obsproject.com/wiki/Stream-Buffering-Issues"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def browsersource(self,message,*,extra_text=""):
      factoid = """The Browser Source plugin for Windows and macOS are bundled with the installers, go to http://obsproject.com/download/
The browser is included in the stable Ubuntu PPA with version 26.0.0"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def botrepo(self,message,*,extra_text=""):
      factoid = """You wouldn't want to see my code."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def bigsur(self,message,*,extra_text=""):
      factoid = """If you are having issues with OBS Studio on macOS Big Sur, make sure you have updated to the latest version, as many of the issues were resolved in v26.1.2.
Select Help -> Check For Updates in OBS, or the newest version can be manually downloaded here: https://obsproject.com/download"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def bestsettings(self,message,*,extra_text=""):
      factoid = """There are no "best settings." Please understand that every setup, for every use case, will be very different. Any guides or videos that claim otherwise are misinforming. Your best option is to start with a base and adjust as necessary. Test, test, and test again. We are happy to offer suggestions for any issues you may be having, but we will not give you a list of settings."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def avast(self,message,*,extra_text=""):
      factoid = """The Avast/AVG antivirus' Game Mode is known to cause issues with OBS. Having it enabled will essentially render OBS inoperable. You can either disable Game Mode in the options, or uninstall Avast/AVG completely."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def autoconfig(self,message,*,extra_text=""):
      factoid = """Please run the OBS auto-configuration tool. To use the auto-config, click on the Tools menu in OBS, select Auto-Configuration Wizard, and then just follow the on-screen directions. You can use this tool to get a set baseline settings for your hardware, and adjust as necessary from there."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def asio(self,message,*,extra_text=""):
      factoid = """An ASIO input plugin is available for OBS: https://github.com/Andersama/obs-asio"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def antivirus(self,message,*,extra_text=""):
      factoid = """Problems with disappearing files, the installation of OBS, or the installation of plugins? Some anti-virus programs are known to flag new files as potentially dangerous, even when the files are completely safe. The heuristic scanning doesn't know that and can quarantine those files anyway. Use less paranoid anti-virus software, or whitelist/exclude the OBS folder from scanning."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def analyze(self,message,*,extra_text=""):
      factoid = """Twitch Stream Analyzer - https://r-1.ch/analyzer/"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def amfdrivers(self,message,*,extra_text=""):
      factoid = """Due to an increase in crash reports usually from users with old or even ancient (>1 year out of date) drivers, the decision was made to no longer load the plugin on those systems. This also reduced the amount of code necessary to maintain as backwards compatibility is only necessary for the UI instead of both the UI and the encoder. The recommended version is 19.9.2 or newer."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def aero(self,message,*,extra_text=""):
      factoid = """Windows Aero is a system setting on Windows 7 that enables enhanced graphical effects and allows Window Capture in OBS to function better. Disabling Aero can also improve Display Capture performance. Aero does not need to be enabled or disabled for capture to work on Windows 8 or newer.
How to enable or disable Aero in Windows 7"""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def adminshares(self,message,*,extra_text=""):
      factoid = """In order to access network shares when OBS is run as administrator, additional configuration of Windows is required:
https://support.microsoft.com/kb/3035277
NOTE: This may lower the security of your system, so please make sure you understand the changes before making them."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def admin(self,message,*,extra_text=""):
      factoid = """Certain games or applications will require OBS Studio to be run with elevated privileges (Administrator) in order to be captured. Running as administrator may also improve OBS performance when gaming.
To run as administrator, close OBS Studio, then simply right click the OBS Studio shortcut and select Run as administrator."""
      await factoids_execution.execute(self, message,factoid,extra_text)

    @commands.command()
    async def ad(self,message,*,extra_text=""):
      factoid = """Self-advertisement or advertisement for others is only  allowed on this server in <#474040782995587082>. Please read the rules in the <#477179447485661186> channel."""
      await factoids_execution.execute(self, message,factoid,extra_text)









    async def execute(self, message,factoid,extra_text=None):
            reference = message.message.reference
            
            message_parts = extra_text.split()
            # attempt to delete the message requesting the factoid if it's within a reply and only contains command
            if reference and len(message_parts) == 0:
                await message.message.delete(delay=0.0)

            # if users are mentioned (but it's not a reply), mention them in the bot reply as well
            user_mention = None

            if message.message.mentions and not reference:
                user_mention = ' '.join(user.mention for user in message.message.mentions)

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

            if message.message.reference and embed is not None:
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




def setup(client):
  client.add_cog(factoids_execution(client))