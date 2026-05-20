from authorization import bot
from pyrogram import filters

ADMIN = "Lazy_Reo"
WLC_TEMPLATE = "{}Welcome to Kurigram Learning Session: {}"


@bot.on_message(filters.command("start"))
async def start(client, message):
    chat = message.chat
    response = await chat.ask("Hey user, what is your name?")
    name = response.text
    response = await chat.ask(f"Hello {name}, what is your age?")
    age = response.text
    text = WLC_TEMPLATE.format("✨", (message.from_user.mention))
    await message.reply(text)
    await bot.send_message(ADMIN, f"""You have officially joined the Kurigram learning session!
Name: {name}
Age: {age}""")


bot.run()
