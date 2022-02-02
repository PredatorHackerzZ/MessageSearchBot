# (c) @PredatorHackerzZ

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "PHListBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is a TeleGram BotList Search Bot of @TheTeleRoid And Some Other Bots Available On TeleGram.

🤖 My Name: <a href='https://t.me/PHListBot'> @PHListBot </a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram </a>

📡 Server: <a href='https://heroku.com'> Heroku </a>

👨‍💻 Modified By: <a href='https://t.me/PredatorHackerzZ'>@HelpLessBoi</a>

🌀 Github Repo: <a href='https://github.com/PredatorHackerzZ/MessageSearchBot'>Click Me</a>

👥 Bots Support: <a href='https://t.me/teleroid14'>@TeleRoid14</a>

📢 Bots Updates: <a href='https://t.me/teleroidgroup'>@TeleRoidGroup</a></b>
"""
    
    ABOUT_HELP_TEXT = """<b>👨‍💻 Developers : <a href='https://t.me/PredatorHackerzZ'>@𝐏𝐫𝐞𝐝𝐚𝐭𝐨𝐫𝐇𝐚𝐜𝐤𝐞𝐫𝐳𝐙</a>

Bots are simply Telegram accounts operated by software – not people – and they'll often have AI features. They can do anything – teach, play, search, broadcast, remind, connect, integrate with other services, or even pass commands to the Internet of Things.

Choose Your Bot Category Here 🤗

☛ RENAMER_BOTS
☛ FILE_TO_LINK_BOTS
☛ GDRIVE_BOTS
☛ URL_UPLOADER_BOTS
☛ YOUTUBE_DOWNLOAD_BOTS
☛ FILE_CONVERTOR_BOTS
☛ UNZIP_BOTS
☛ SCREENSHOT_BOT
☛ GOOGLE_TRANSLATION_BOTS
☛ TORRENT_DOWNLOADER_BOTS
☛ DMCA_REMOVAL_BOTS
☛ WATERMARK_BOT
☛ VIDEO_MERGER_BOTS

**These Bots can Do Multiple things with different Functions**:-

🌀 I will help you to find Best Telegram Bots.

🌀 If you Get Any Error In Searching Please Report at **@TeleRoid14**.

🌀 Our Project Channel: <a href='https://t.me/TeleRoidGroup'>@TeleRoidGroup</a>.

🌀 All Bots Based On Users and Developer Demands. 

🤖 Join For All Available Bots On Telegram: @TGRobot_List.
"""
    
    HOME_TEXT = """
<b>👋 Hey !{}, This is Online Search Botlist Bot <a href='https://t.me/PHListBot'>@PHListBot</a>.

<a> Modified By : @PredatorHackerzZ</a>

       <a> Credits goes to Everyone Who Supported.</b>

<a> Made With ❤ By @TheTeleRoid </a>
"""


    START_MSG = """
<b>👋 Hey !{}, This is Online Search Botlist Bot <a href='https://t.me/PHListBot'>@PHListBot</a>.

<a> Modified By : @PredatorHackerzZ</a>

       <a> Credits goes to Everyone Who Supported.</b>

<a> Made With ❤ By @TheTeleRoid </a>
"""
    ADD_BOTS = """<b>Heya! {} If You Want to Add Your Bots In @PHListBot then Contact Admin From Below Given Groups</b>"""


