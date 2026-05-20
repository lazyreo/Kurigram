from authorization import bot
import pyrogram
import api_client as api
import config



@bot.on_message(pyrogram.filters.text, group=1)
async def check_participant(client, message):
    try:
        await client.get_chat_member(config.MY_CHANNEL_ID, message.from_user.id)
        raise pyrogram.ContinuePropagation
    except pyrogram.errors.UserNotParticipant:
        await message.reply(text="🚨**Join this Channel to utilize this BOT**‼️", parse_mode=pyrogram.enums.ParseMode.MARKDOWN, reply_markup=pyrogram.types.InlineKeyboardMarkup(
            [
                [
                    pyrogram.types.InlineKeyboardButton
                    (
                        text="Join",
                        url="https://t.me/practicekurigram"
                    )
                ]
            ]
        ))
        raise  pyrogram.StopPropagation
        
@bot.on_message(~pyrogram.filters.regex(r"^https"), group=2)
async def anyothermessage(client, message):
    await message.reply(text=f"** Hello {message.from_user.first_name}, send me a lengthy URL and I will shorten it❗️**", parse_mode=pyrogram.enums.ParseMode.MARKDOWN)
    

@bot.on_message(pyrogram.filters.regex(r"^https"), group=2)
async def url(client, message):    
    url_msg = message.text
    
    params = {
        "api": config.DROPLINK_API_KEY,
        "url": url_msg
    }
    headers = {
        "User-Agent": "Telegram_URL_BOT/1.0 (contact: reoefrin67@gmail.com)",
        "Accept": "application/json"
    }

    response = api.get_json_response(
        url="https://droplink.co/api", params=params, headers=headers)
    shortened_url = response.get("shortenedUrl")
    await message.reply(
        text=f"`{shortened_url}`",
        parse_mode=pyrogram.enums.ParseMode.MARKDOWN,
        reply_markup=pyrogram.types.InlineKeyboardMarkup(
            [
                [
                    pyrogram.types.InlineKeyboardButton
                    (
                        text="Open",
                        url=shortened_url
                    )
                ]
            ]
        )
    )
    

bot.run()
