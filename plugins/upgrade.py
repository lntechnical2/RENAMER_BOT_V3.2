from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daly  Upload limit 2GB
	Price 0 
	
	**VIP 1 ** 
	Daly Upload  limit 10GB
	Price Rs 55 🇮🇳/🌎 0.67$  per Month
	
	**VIP 2 **
	Daly Upload limit 5OGB
	Price Rs 150 🇮🇳/🌎 1.82$  per Month
	
	Pay Using Upi I'd ```lokamandc1224@oksbi```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/mrlokaman")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://www.paypal.me/lokamanchendekar"),
        			InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/los89jy0")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
