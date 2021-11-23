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
    ABOUT_BOT_TEXT = """<b>**This is a TeleGram BotList Search Bot of @TheTeleRoid And Some Other Bots Available On TeleGram**.

🤖 **My Name**: <a href='https://t.me/PHListBot'>@𝐏𝐇𝐋𝐢𝐬𝐭𝐁𝐨𝐭</a>

📜 **Language** : <a href='https://www.python.org'>𝐏𝐲𝐭𝐡𝐨𝐧𝟑</a>

📚 **Library** : <a href='https://docs.pyrogram.org'>𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦</a>

📡 **Hosting Server**: <a href='https://heroku.com'>𝐇𝐞𝐫𝐨𝐤𝐮</a>

👨‍💻 **Developed By**: <a href='https://t.me/PredatorHackerzZ'>@𝐏𝐫𝐞𝐝𝐚𝐭𝐨𝐫𝐇𝐚𝐜𝐤𝐞𝐫𝐳𝐙</a>

💢 **Github Repo**: <a href='https://github.com/PredatorHackerzZ/MessageSearchBot'>𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞</a>

👥 **Bot Support**: <a href='https://t.me/teleroid14'>@𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝𝐒𝐮𝐩𝐩𝐨𝐫𝐭</a>

📢 **Bot Updates**: <a href='https://t.me/teleroidgroup'>@𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝𝐆𝐫𝐨𝐮𝐩</a></b>
"""
    
    ABOUT_HELP_TEXT = """<b>👨‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫: <a href='https://t.me/PredatorHackerzZ'>@𝐏𝐫𝐞𝐝𝐚𝐭𝐨𝐫𝐇𝐚𝐜𝐤𝐞𝐫𝐳𝐙</a>

Bots are simply Telegram accounts operated by software – not people – and they'll often have AI features. They can do anything – teach, play, search, broadcast, remind, connect, integrate with other services, or even pass commands to the Internet of Things.

Choose Your Bot Category Here 🤗

☛ RENAMER_BOTS
☛ FILE_TO_LINK_BOTS
☛ GDRIVE_BOTS
☛ URL_UPLOADER_BOTS
☛ GROUP_MANAGER_BOTS
☛ ZEE5_DOWNLOADER_BOTS
☛ YOUTUBE_DOWNLOAD_BOTS
☛ FILE_CONVERTOR_BOTS
☛ INSTAGRAM_BOTS
☛ UNZIP_BOTS
☛ MOVIE_SEARCHBOT
☛ AUTOFILTER_BOT
☛ SCREENSHOT_BOT
☛ GOOGLE_TRANSLATION_BOTS
☛ TORRENT_DOWNLOADER_BOTS
☛ DMCA_REMOVAL_BOTS
☛ WATERMARK_BOT
☛ PDISK_UPLOADER_BOTS
☛ VIDEO_MERGER_BOTS

**These Bots can Do Multiple things with different Functions**:-

🌀 𝐈 𝐜𝐚𝐧 𝐠𝐞𝐭 𝐲𝐨𝐮 𝐁𝐞𝐬𝐭 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐁𝐨𝐭𝐬 𝐮𝐧𝐝𝐞𝐫 𝐓𝐞𝐥𝐞𝐆𝐫𝐚𝐦 𝐁𝐨𝐭𝐬 𝐏𝐫𝐨𝐣𝐞𝐜𝐭𝐬.

🌀 𝐈𝐟 𝐮 𝐆𝐞𝐭 𝐚𝐧𝐲 𝐄𝐫𝐫𝐨𝐫 𝐑𝐞𝐠𝐚𝐫𝐝𝐢𝐧𝐠 𝐁𝐨𝐭𝐬 𝐢𝐧 𝐭𝐡𝐞 𝐁𝐨𝐭𝐥𝐢𝐬𝐭 .𝐑𝐞𝐩𝐨𝐫𝐭 : <a href='https://t.me/teleroid14'>@𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝𝟏𝟒</a>.

🌀 𝐎𝐮𝐫 𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : <a href='https://t.me/TeleRoidGroup'>𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝𝐆𝐫𝐨𝐮𝐩</a>.

🌀🎦 𝐀𝐥𝐥 𝐁𝐨𝐭𝐬 𝐁𝐚𝐬𝐞𝐝 𝐨𝐧 𝐲𝐨𝐮𝐫 𝐈𝐧𝐭𝐞𝐫𝐞𝐬𝐭 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐮𝐩𝐥𝐨𝐚𝐝𝐞𝐝. 𝐘𝐨𝐮 𝐜𝐚𝐧 𝐬𝐞𝐧𝐝 𝐲𝐨𝐮𝐫 𝐟𝐞𝐞𝐝𝐛𝐚𝐜𝐤 𝐭𝐨 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩.

📢𝐉𝐨𝐢𝐧 : <a href='https://t.me/TheTeleRoid'>**@TeleRoid14**</a></b>
"""
    
    HOME_TEXT = """
<b>𝐇𝐞𝐲!, {}, 𝐓𝐡𝐢𝐬 𝐈𝐬 𝐈𝐧𝐥𝐢𝐧𝐞 𝐁𝐨𝐭𝐋𝐢𝐬𝐭 𝐒𝐞𝐚𝐫𝐜𝐡 𝐁𝐨𝐭 <a href='https://t.me/PHListBot'>@𝐏𝐇𝐋𝐢𝐬𝐭𝐁𝐨𝐭</a>.

𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 : <a href='https://t.me/TheTeleRoid'>𝐎𝐰𝐧𝐞𝐫_𝐁𝐨𝐭</a>

           𝐄𝐯𝐞𝐫𝐲𝐎𝐧𝐞 𝐈𝐧 𝐓𝐡𝐢𝐬 𝐉𝐨𝐮𝐫𝐧𝐞𝐲.</b>
"""


    START_MSG = """<b>𝐇𝐞𝐥𝐥𝐨!, {}, 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐀𝐧 𝐀𝐦𝐚𝐳𝐢𝐧𝐠 𝐈𝐧𝐥𝐢𝐧𝐞 𝐁𝐨𝐭 𝐒𝐞𝐚𝐫𝐜𝐡 𝐑𝐨𝐛𝐨𝐭 𝐭𝐡𝐚𝐭 𝐟𝐢𝐧𝐝𝐬 𝐀𝐦𝐚𝐳𝐢𝐧𝐠 𝐁𝐨𝐭𝐬 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐨𝐧 𝐓𝐞𝐥𝐞𝐆𝐫𝐚𝐦.</b>

<b>𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐅𝐨𝐫 :</b> @TeleRoidGroup ; 𝐌𝐮𝐬𝐭 𝐉𝐨𝐢𝐧 𝐓𝐡𝐢𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥. 

𝐌𝐚𝐝𝐞 𝐰𝐢𝐭𝐡 ❤ 𝐅𝐫𝐨𝐦 <a href='https://t.me/TheTeleRoid'>@TʜᴇTᴇʟᴇʀᴏɪᴅ</a>"""

    ADD_BOTS = """<b>**Heya! {} If You Want to Add Your Bots In @PHListBot then Contact Admin From Below Given Groups**</b>"""


