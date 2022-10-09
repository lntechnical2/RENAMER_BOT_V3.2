import os
from pyrogram import Client, filters
from helper.premiumdb import add_premium 
from helper.date import add_date
ADMIN = int(os.environ.get("ADMIN", 923943045))
 
@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["addpremium"]))
async def buypremium(bot, message):
	id = message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	date = add_date()
	add_premium(user_id)
	await message.reply_text("Added successfully",quote=True)
		
