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

π€ My Name: <a href='https://t.me/PHListBot'> @PHListBot </a>

π Language : <a href='https://www.python.org'> Python V3</a>

π Library: <a href='https://docs.pyrogram.org'> Pyrogram </a>

π‘ Server: <a href='https://heroku.com'> Heroku </a>

π¨βπ» Modified By: <a href='https://t.me/PredatorHackerzZ'>@HelpLessBoi</a>

π Github Repo: <a href='https://github.com/PredatorHackerzZ/MessageSearchBot'>Click Me</a>

π₯ Bots Support: <a href='https://t.me/teleroid14'>@TeleRoid14</a>

π’ Bots Updates: <a href='https://t.me/teleroidgroup'>@TeleRoidGroup</a></b>
"""
    
    ABOUT_HELP_TEXT = """<b>π¨βπ» Developers : <a href='https://t.me/PredatorHackerzZ'>@ππ«ππππ­π¨π«ππππ€ππ«π³π</a>

BotsΒ are simply Telegram accounts operated by software β not people β and they'll often have AI features. They can do anything β teach, play, search, broadcast, remind, connect, integrate with other services, or even pass commands to the Internet of Things.

Choose Your Bot Category Here π€

β RENAMER_BOTS
β FILE_TO_LINK_BOTS
β GDRIVE_BOTS
β URL_UPLOADER_BOTS
β YOUTUBE_DOWNLOAD_BOTS
β FILE_CONVERTOR_BOTS
β UNZIP_BOTS
β SCREENSHOT_BOT
β GOOGLE_TRANSLATION_BOTS
β TORRENT_DOWNLOADER_BOTS
β DMCA_REMOVAL_BOTS
β WATERMARK_BOT
β VIDEO_MERGER_BOTS

**These Bots can Do Multiple things with different Functions**:-

π I will help you to find Best Telegram Bots.

π If you Get Any Error In Searching Please Report at **@TeleRoid14**.

π Our Project Channel: <a href='https://t.me/TeleRoidGroup'>@TeleRoidGroup</a>.

π All Bots Based On Users and Developer Demands. 

π€ Join For All Available Bots On Telegram: @TGRobot_List.
"""
    
    HOME_TEXT = """
<b>π Hey !{}, This is Online Search Botlist Bot <a href='https://t.me/PHListBot'>@PHListBot</a>.

<a> Modified By : @PredatorHackerzZ</a>

       <a> Credits goes to Everyone Who Supported.</b>

<a> Made With β€ By @TheTeleRoid </a>
"""


    START_MSG = """
<b>π Hey !{}, This is Online Search Botlist Bot <a href='https://t.me/PHListBot'>@PHListBot</a>.

<a> Modified By : @PredatorHackerzZ</a>

       <a> Credits goes to Everyone Who Supported.</b>

<a> Made With β€ By @TheTeleRoid </a>
"""
    ADD_BOTS = """<b>Heya! {} If You Want to Add Your Bots In @PHListBot then Contact Admin From Below Given Groups</b>"""


