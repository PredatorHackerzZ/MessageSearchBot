# (c) @PredatorHackerzZ
# I just made this for searching a channel message from inline.
# Maybe you can use this for something else.
# I first made this for @TGBotListBot ...
# Edit according to your use.

from configs import Config
from pyrogram import Client, filters, idle
from pyrogram.errors import QueryIdInvalid
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent

# Bot Client for Inline Search
Bot = Client(
    session_name=Config.BOT_SESSION_NAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

# User Client for Searching in Channel.
User = Client(
    session_name=Config.USER_SESSION_STRING,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)


@Bot.on_message(filters.private & filters.command("start"))
async def start_handler(_, event: Message):
    await event.reply_text(Config.START_MSG.format(event.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("𝐁𝐨𝐭𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url="https://t.me/TeleRoidGroup"),
             InlineKeyboardButton("𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩", url="https://t.me/TeleRoid14")],
            [InlineKeyboardButton("♻ 𝐇𝐞𝐥𝐩", callback_data="Help_msg"),
             InlineKeyboardButton("👥 𝐀𝐛𝐨𝐮𝐭", callback_data="About_msg")],
            [InlineKeyboardButton("𝐀𝐝𝐝 𝐘𝐨𝐮𝐫 𝐁𝐨𝐭𝐋𝐢𝐬𝐭 𝐇𝐞𝐫𝐞",url="https://t.me/TeleRoid14")],
            [InlineKeyboardButton("𝐒𝐞𝐚𝐫𝐜𝐡 𝐈𝐧𝐥𝐢𝐧𝐞", switch_inline_query_current_chat=""), InlineKeyboardButton("𝐆𝐨 𝐈𝐧𝐥𝐢𝐧𝐞", switch_inline_query="")]
        ])
    )


@Bot.on_inline_query()
async def inline_handlers(_, event: InlineQuery):
    answers = list()
    # If Search Query is Empty
    if event.query == "":
        answers.append(
            InlineQueryResultArticle(
                title="This is Inline Messages Search Bot!",
                description="You can search Channel All Messages using this bot.",
                input_message_content=InputTextMessageContent(
                    message_text="𝐔𝐬𝐢𝐧𝐠 𝐭𝐡𝐢𝐬 𝐁𝐨𝐭 𝐲𝐨𝐮 𝐜𝐚𝐧 𝐒𝐞𝐚𝐫𝐜𝐡 𝐚𝐥𝐥 𝐭𝐡𝐞 𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝 𝐁𝐨𝐭𝐋𝐢𝐬𝐭 𝐁𝐨𝐭 𝐚𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐎𝐧 𝐓𝐞𝐥𝐞𝐆𝐫𝐚𝐦.\n\n"
                                 "**Made by the Owner @PredatorHackerzZ**\n**@TheTeleRoid**",
                    disable_web_page_preview=True
                ),
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("𝐒𝐞𝐚𝐫𝐜𝐡 𝐇𝐞𝐫𝐞", switch_inline_query_current_chat="")],
                    [InlineKeyboardButton("𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝 𝐁𝐨𝐭𝐋𝐢𝐬𝐭", url="https://t.me/joinchat/t1ko_FOJxhFiOThl"),
                     InlineKeyboardButton("𝐁𝐨𝐭𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url="https://t.me/TeleRoidGroup")],
                    [InlineKeyboardButton("𝐓𝐞𝐥𝐞𝐆𝐫𝐚𝐦 𝐁𝐨𝐭𝐬𝐋𝐢𝐬𝐭", url="https://t.me/TGRobot_List")]
                ])
            )
        )
    # Search Channel Message using Search Query Words
    else:
        async for message in User.search_messages(chat_id=Config.CHANNEL_ID, limit=50, query=event.query):
            if message.text:
                answers.append(InlineQueryResultArticle(
                    title="{}".format(message.text.split("\n", 1)[0]),
                    description="{}".format(message.text.split("\n", 2)[-1]),
                    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝐒𝐞𝐚𝐫𝐜𝐡 𝐀𝐠𝐚𝐢𝐧", switch_inline_query_current_chat=""), InlineKeyboardButton("𝐆𝐨 𝐈𝐧𝐥𝐢𝐧𝐞", switch_inline_query="")]]),
                    input_message_content=InputTextMessageContent(
                        message_text=message.text.html,
                        parse_mode="html",
                        disable_web_page_preview=True
                    )
                ))
    try:
        await event.answer(
            results=answers,
            cache_time=0
        )
        print(f"[{Config.BOT_SESSION_NAME}] - Answered Successfully - {event.from_user.first_name}")
    except QueryIdInvalid:
        print(f"[{Config.BOT_SESSION_NAME}] - Failed to Answer - {event.from_user.first_name}")


@Bot.on_callback_query()
async def button(bot, cmd: CallbackQuery):
	cb_data = cmd.data
	if "About_msg" in cb_data:
            await cmd.message.edit(
			text=Config.ABOUT_BOT_TEXT,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("📢 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞 ", url="https://t.me/Moviesflixers_DL")
					],
					[
						InlineKeyboardButton("🏠 𝐇𝐨𝐦𝐞", callback_data="gohome"),
						InlineKeyboardButton("👮 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫", url="https://t.me/TheTeleRoid")
					]
				]
			),
			parse_mode="html"
		)
	elif "Help_msg" in cb_data:
            await cmd.message.edit(
			text=Config.ABOUT_HELP_TEXT,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞𝐬 𝐨𝐟 𝐁𝐨𝐭", url="https://t.me/Moviesflixers_DL")
					],
					[
						InlineKeyboardButton("👥 𝐀𝐛𝐨𝐮𝐭", callback_data="About_msg"),
						InlineKeyboardButton("🏠 𝐇𝐨𝐦𝐞", callback_data="gohome")
					]
				]
			),
			parse_mode="html"
		)
	elif "gohome" in cb_data:
	    await cmd.message.edit(
			text=Config.START_MSG.format(cmd.from_user.mention),
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton("🛑 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🛑", url="https://t.me/TeleRoid14"),
						InlineKeyboardButton("⭕ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ⭕", url="https://t.me/TeleRoidGroup")
					],
					[
						InlineKeyboardButton("👥 𝐀𝐛𝐨𝐮𝐭", callback_data="About_msg"),
						InlineKeyboardButton("♻ 𝐇𝐞𝐥𝐩", callback_data="Help_msg")
					]
				]
			),
			parse_mode="html"
		)


# Start Clients
Bot.start()
User.start()
# Loop Clients till Disconnects
idle()
# After Disconnects,
# Stop Clients
Bot.stop()
User.stop()
