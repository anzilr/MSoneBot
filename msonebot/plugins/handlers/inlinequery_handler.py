from pyrogram.types import *
from pyrogram import Client
from msonebot.logging import LOGGER
from msonebot.helpers.msoneapi import MSoneAPI
import numpy as np


msone = MSoneAPI


@Client.on_inline_query()
async def inlinequery(client, inline_query):
    query = inline_query.query
    print(query)
    resultss = []

    if len(query) == 0:
        return

    else:
        try:

            results = msone.get_results(query)
            k = 0
            for i in np.arange(len(results)):
                sub_result = (results[k])
                relno = (sub_result['release_number'])
                title = (sub_result['title'])
                sub_url = (sub_result['subtitle_url'])
                poster_link = (sub_result['poster_link'])
                thumb_link = (sub_result['thumb_link'])
                poster_name = (sub_result['poster_name'])
                poster_bio = (sub_result['poster_bio'])
                translators = (sub_result['translators'])
                language = (sub_result['language'])
                direction = (sub_result['direction'])
                genre = (sub_result['genre'])
                url = (sub_result['url'])
                resultss.append(
                    InlineQueryResultPhoto(
                        photo_url=poster_link,
                        caption=f'''<b>{title}</b>\n\n<b>[MSone](https://malayalamsubtitles.org/)</b> Release - {relno}\n\n{language}\n{direction}\n{translators}\n{genre}\nപോസ്റ്റർ : [{poster_name}]({poster_bio})\n\nClick below 👇🏻 for synopsis''',
                        title=title,
                        description=f"MSone Release {relno}\n{language}\n{genre}",
                        thumb_url=f"{thumb_link}",
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [InlineKeyboardButton(text="📲 Download Subtitle", url=sub_url)],
                                [InlineKeyboardButton(text="📝 Synopsis", callback_data=f"synopy{relno}")],
                                [InlineKeyboardButton(text="🔍 Search", switch_inline_query_current_chat=""),
                                 InlineKeyboardButton(text="🔗 Visit", url=url)]

                            ]
                        )
                    )

                )
                k += 1
                if k == 50:
                    break

        except Exception as e:
            LOGGER(__name__).info(e)

            resultss.append(InlineQueryResultArticle(
                title=("Sorry No Results Found!"),
                input_message_content=InputTextMessageContent("Check your spelling and try again."),
                description=("Check the spelling."),
                thumb_url="https://img.freepik.com/free-vector/oops-404-error-with-broken-robot-concept-illustration_114360-1920.jpg?w=2000"))
            print(e)

        await client.answer_inline_query(

            inline_query_id=inline_query.id,
            results=resultss)