from pyrogram import Client
import requests
from msonebot import LOGGER
from msonebot.config import *
from pyrogram.types import *
import traceback
import numpy as np
from msonebot.helpers.msoneapi import MSoneAPI

s = requests.Session()
msone = MSoneAPI


@Client.on_message()
async def msgHandler(client, message):
    if message.text is None:
        pass
    else:
        try:
            query = message.text
            print(query)
            userid = message.from_user.id
            results1 = msone.get_results(query)
            buttons = []
            check_title = []
            j = 0
            for t in np.arange(len(results1)):
                title1 = results1[j]
                title2 = (title1['title'])
                check_title.append(title2)
                j += 1
                if j == 100:
                    break
            k = 0
            if [check_title[0]] * len(check_title) == check_title:
                for i in np.arange(len(results1)):
                    sub_result = (results1[k])
                    releaseno = (sub_result['release_number'])
                    title = (sub_result['title'])
                    subtitle_url = (sub_result['subtitle_url'])
                    poster_link = (sub_result['poster_link'])
                    thumb_link = (sub_result['thumb_link'])
                    '''r = s.head(poster_link)
                    scode = r.status_code
                    if scode != 200:
                        poster_link = thumb_link'''
                    poster_name = (sub_result['poster_name'])
                    poster_bio = (sub_result['poster_bio'])
                    translators = (sub_result['translators'])
                    language = (sub_result['language'])
                    direction = (sub_result['direction'])
                    genre = (sub_result['genre'])
                    url = (sub_result['url'])

                    await client.send_photo(chat_id=userid,
                                            photo=poster_link,
                                            caption=(
                                                f"<b>{title}</b>\n\n<b>[MSone](https://malayalamsubtitles.org/)</b> Release - {releaseno}\n\n{language}\n{direction}\n{translators}\n{genre}\nപോസ്റ്റർ : [{poster_name}]({poster_bio})\n\nClick below 👇🏻 for synopsis"),
                                            reply_markup=InlineKeyboardMarkup([
                                                [InlineKeyboardButton(text="📲 Download Subtitle", url=subtitle_url)],
                                                [InlineKeyboardButton(text="📝 Synopsis",
                                                                      callback_data=f"synopy{releaseno}")],
                                                [InlineKeyboardButton(text="🔍 Search",
                                                                      switch_inline_query_current_chat=""),
                                                 InlineKeyboardButton(text="🔗 Visit", url=url)]]))
                    k += 1


            else:
                for i in np.arange(len(results1)):
                    sub_result = (results1[k])
                    title = (sub_result['title'])
                    buttons.append([KeyboardButton(text=f"{title}")])
                    k += 1
                    if k == 99:
                        break

            if buttons:
                msg = await client.send_message(chat_id=userid,
                                                text="Click on a title below.",
                                                reply_markup=ReplyKeyboardMarkup(buttons,
                                                                                 one_time_keyboard=True,
                                                                                 selective=True,
                                                                                 placeholder="Click on a title below👇🏻"))

        except Exception:
            LOGGER(__name__).error(traceback.format_exc())
            await client.send_message(chat_id=LOG_CHANNEL, text=f'"`{traceback.format_exc()}"`')
