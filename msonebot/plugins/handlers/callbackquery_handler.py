from pyrogram import Client, filters
from msonebot.helpers.msoneapi import MSoneAPI

msone = MSoneAPI


@Client.on_callback_query(filters.regex("synopy"))
async def SynopyHandler(client, CallbackQuery):
    query = CallbackQuery.data
    if query is None:
        return
    else:
        try:
            dl, releaseno = query.split("synopy")
            synopi = msone.get_synopsis(releaseno)
            lines = synopi.split("|")
            synopi = (f"\n\n".join(lines))
        except:
            synopi = "Sorry, no synopsis available."
    await client.send_message(chat_id=CallbackQuery.from_user.id, text=synopi)
