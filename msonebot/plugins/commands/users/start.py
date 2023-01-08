from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from msonebot.assets.start_constants import *
from pyrogram import Client, filters
from msonebot.config import *
from urllib.parse import quote

btext = 't.me/share/url?url=' + quote(
    "Hey, Check out @msonesubsbot to download malayalam subtitles of movies and series.")

START_BUTTON = [
    [
        InlineKeyboardButton("📖 Commands", callback_data="COMMAND_BUTTON"),
        InlineKeyboardButton("🧞‍♂ Help", callback_data="HELP_BUTTON"),
    ],
    [
        InlineKeyboardButton("⤴️ Share", url=btext),
        InlineKeyboardButton("👨‍💻 About me", callback_data="ABOUT_BUTTON")
    ],
    [
        InlineKeyboardButton(text="🔍 Search", switch_inline_query_current_chat="")
    ]
]

COMMAND_BUTTON = [
    [
        InlineKeyboardButton("👥 Users", callback_data="USER_BUTTON"),
    ],
    [InlineKeyboardButton("🔙 Go Back", callback_data="START_BUTTON")],
]

HELP_BUTTON = [

    [InlineKeyboardButton(text="🔍 Search", switch_inline_query_current_chat="")],
    [InlineKeyboardButton("🔙 Go Back", callback_data="START_BUTTON")]
]

GOBACK_1_BUTTON = [[InlineKeyboardButton("🔙 Go Back", callback_data="START_BUTTON")]]

GOBACK_2_BUTTON = [[InlineKeyboardButton("🔙 Go Back", callback_data="COMMAND_BUTTON")]]

commands = ["start", "help"]


@Client.on_message(filters.command(commands, **prefixes))
async def start(client, message):
    await message.reply_photo(
        photo=START_PHOTO,
        caption=START_CAPTION,
        reply_markup=InlineKeyboardMarkup(START_BUTTON),
        quote=True)


@Client.on_callback_query(filters.regex("_BUTTON"))
async def botCallbacks(client, CallbackQuery):
    clicker_user_id = CallbackQuery.from_user.id
    user_id = CallbackQuery.message.reply_to_message.from_user.id

    if clicker_user_id != user_id:
        return await CallbackQuery.answer("⚠️ This command is not initiated by you.")

    if CallbackQuery.data == "ABOUT_BUTTON":
        await CallbackQuery.edit_message_text(ABOUT_CAPTION, reply_markup=InlineKeyboardMarkup(GOBACK_1_BUTTON))
    elif CallbackQuery.data == "HELP_BUTTON":
        await CallbackQuery.edit_message_text(HELP_CAPTION, reply_markup=InlineKeyboardMarkup(HELP_BUTTON))

    elif CallbackQuery.data == "START_BUTTON":
        await CallbackQuery.edit_message_text(START_CAPTION, reply_markup=InlineKeyboardMarkup(START_BUTTON))

    elif CallbackQuery.data == "COMMAND_BUTTON":
        await CallbackQuery.edit_message_text(COMMAND_CAPTION, reply_markup=InlineKeyboardMarkup(COMMAND_BUTTON))

    elif CallbackQuery.data == "USER_BUTTON":
        await CallbackQuery.edit_message_text(USER_TEXT, reply_markup=InlineKeyboardMarkup(GOBACK_2_BUTTON))

    elif CallbackQuery.data == "SUDO_BUTTON":
        if clicker_user_id not in SUDO_USERID:
            return await CallbackQuery.answer("⚠️ You are not authorised to use Admin commands.", show_alert=True)
        else:
            await CallbackQuery.edit_message_text(SUDO_TEXT, reply_markup=InlineKeyboardMarkup(GOBACK_2_BUTTON))

    elif CallbackQuery.data == "DEV_BUTTON":
        if clicker_user_id not in OWNER_USERID:
            return await CallbackQuery.answer("⚠️ Only the bot developer can use these commands.", show_alert=True)
        else:
            await CallbackQuery.edit_message_text(DEV_TEXT, reply_markup=InlineKeyboardMarkup(GOBACK_2_BUTTON))
