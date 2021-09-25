# (c) @PredatorHackerzZ

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "PHListBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    ABOUT_BOT_TEXT = """<b>
𝐓𝐡𝐢𝐬 𝐢𝐬 𝐀 𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝 𝐁𝐨𝐭𝐋𝐢𝐬𝐭 𝐒𝐞𝐚𝐫𝐜𝐡 𝐁𝐨𝐭 𝐎𝐟 @TheTeleRoid 𝐀𝐧𝐝 𝐒𝐨𝐦𝐞 𝐎𝐭𝐡𝐞𝐫 𝐁𝐨𝐭𝐬 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐎𝐧 𝐓𝐞𝐥𝐞𝐆𝐫𝐚𝐦.

🤖 𝗠𝘆 𝗡𝗮𝗺𝗲: <a href='https://t.me/PHListBot'>@𝐏𝐇𝐋𝐢𝐬𝐭𝐁𝐨𝐭</a>

📜 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲: <a href='https://www.python.org'>𝐏𝐲𝐭𝐡𝐨𝐧𝟑</a>

📚 𝗟𝗶𝗯𝗿𝗮𝗿𝘆: <a href='https://docs.pyrogram.org'>𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦</a>

📡 𝗛𝗼𝘀𝘁𝗲𝗱 𝗼𝗻: <a href='https://heroku.com'>𝐇𝐞𝐫𝐨𝐤𝐮</a>

👨‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: <a href='https://t.me/PredatorHackerzZ'>@𝐏𝐫𝐞𝐝𝐚𝐭𝐨𝐫𝐇𝐚𝐜𝐤𝐞𝐫𝐳𝐙</a>

🌐 𝗚𝗶𝘁𝗵𝘂𝗕 𝗥𝗲𝗽𝗼: <a href='https://github.com/PredatorHackerzZ'>𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞</a>

👥 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗚𝗿𝗼𝘂𝗽: <a href='https://t.me/teleroid14'>𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝 𝐒𝐮𝐩𝐩𝐨𝐫𝐭</a>

📢 𝗨𝗽𝗱𝗮𝘁𝗲𝘀 𝗖𝗵𝗮𝗻𝗻𝗲𝗹: <a href='https://t.me/teleroidgroup'>𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝 𝐔𝐩𝐝𝐚𝐭𝐞𝐬</a></b>
"""
    
    ABOUT_HELP_TEXT = """<b>

👨‍💻 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫: <a href='https://t.me/PredatorHackerzZ'>@𝐏𝐫𝐞𝐝𝐚𝐭𝐨𝐫𝐇𝐚𝐜𝐤𝐞𝐫𝐳𝐙</a>


Choose Bot category 😎
☛ RENAME_BOTS
☛ FILE_TO_LINK_BOTS
☛ GDRIVE_BOTS
☛ URL_UPLOADER_BOTS
☛ GROUP_MANAGER_BOTS
☛ MUSIC_SONGS_BOTS
☛ YOUTUBE_BOTS
☛ FILE_CONVERTOR_BOTS
☛ USEFUL_BOTS
☛ LINK_TO_FILE_BOTS


𝗧𝗵𝗲𝗿𝗲 𝗮𝗿𝗲 𝗺𝘂𝗹𝘁𝗶𝗽𝗹𝗲 𝘁𝗵𝗶𝗻𝗴𝘀 𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗰𝗮𝗻 𝗱𝗼:

🌀 𝐈 𝐜𝐚𝐧 𝐠𝐞𝐭 𝐲𝐨𝐮 𝐁𝐞𝐬𝐭 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐁𝐨𝐭𝐬 𝐮𝐧𝐝𝐞𝐫 𝐓𝐞𝐥𝐞𝐆𝐫𝐚𝐦 𝐁𝐨𝐭𝐬 𝐏𝐫𝐨𝐣𝐞𝐜𝐭𝐬.

🌀 𝐈𝐟 𝐮 𝐆𝐞𝐭 𝐚𝐧𝐲 𝐄𝐫𝐫𝐨𝐫 𝐑𝐞𝐠𝐚𝐫𝐝𝐢𝐧𝐠 𝐁𝐨𝐭𝐬 𝐢𝐧 𝐭𝐡𝐞 𝐁𝐨𝐭𝐥𝐢𝐬𝐭 .𝐑𝐞𝐩𝐨𝐫𝐭 : <a href='https://t.me/teleroid14'>@𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝𝟏𝟒</a>.

🌀 𝐎𝐮𝐫 𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : @TeleRoidGroup.

🌀🎦 𝐀𝐥𝐥 𝐁𝐨𝐭𝐬 𝐁𝐚𝐬𝐞𝐝 𝐨𝐧 𝐲𝐨𝐮𝐫 𝐈𝐧𝐭𝐞𝐫𝐞𝐬𝐭 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐮𝐩𝐥𝐨𝐚𝐝𝐞𝐝. 𝐘𝐨𝐮 𝐜𝐚𝐧 𝐬𝐞𝐧𝐝 𝐲𝐨𝐮𝐫 𝐟𝐞𝐞𝐝𝐛𝐚𝐜𝐤 𝐭𝐨 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩.

📢𝐉𝐨𝐢𝐧 : @TheTeleRoid</b>
"""
    
    HOME_TEXT = """
<b>𝐇𝐞𝐲!, {}, 𝐓𝐡𝐢𝐬 𝐈𝐬 𝐁𝐨𝐭𝐋𝐢𝐬𝐭 𝐒𝐞𝐚𝐫𝐜𝐡 𝐁𝐨𝐭 @PHListBot.

𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 : @TeamTeleRoid

           𝐄𝐯𝐞𝐫𝐲𝐎𝐧𝐞 𝐈𝐧 𝐓𝐡𝐢𝐬 𝐉𝐨𝐮𝐫𝐧𝐞𝐲.</b>
"""


    START_MSG = """<b>𝐇𝐞𝐥𝐥𝐨! 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐀𝐧 𝐀𝐦𝐚𝐳𝐢𝐧𝐠 𝐈𝐧𝐥𝐢𝐧𝐞 𝐁𝐨𝐭 𝐒𝐞𝐚𝐫𝐜𝐡 𝐑𝐨𝐛𝐨𝐭 𝐭𝐡𝐚𝐭 𝐟𝐢𝐧𝐝𝐬 𝐀𝐦𝐚𝐳𝐢𝐧𝐠 𝐁𝐨𝐭𝐬 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐨𝐧 𝐓𝐞𝐥𝐞𝐆𝐫𝐚𝐦.</b>

<b>𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 :</b> @PredatorHackerzZ

❤ 𝐅𝐫𝐨𝐦 @TheTeleRoid"""
