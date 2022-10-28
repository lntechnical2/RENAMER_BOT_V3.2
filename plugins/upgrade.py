"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	_____________________________
	**Only Upgrad Upload Limit
	Not Suport 4GB file Rename**
	
	10 GB - 10rs 
	50 GB -  30rs 
	100 GB - 50 rs 
	
	_____________________________
	**It's Support 4GB File Rename**
	**VIP 1 ** 
	Daily  Upload  limit 5GB
	Price Rs 25 🇮🇳/🌎 0.30$  per Month
	
	**VIP 2 **
	Daily Upload limit 1OGB
	Price Rs 35  🇮🇳/🌎 0.42$  per Month
	
	**VIP3**
	Daily Upload limit 30GB
	Price Rs 50  🇮🇳/🌎 0.61$  per Month
	
	**VIP4**
	Daily Upload limit 50GB
	Price Rs 75 🇮🇳/🌎 0.91$  per Month
	
	**VIP**
	Daily Upload limit 100GB 
	Price Rs 110 🇮🇳/🌎 1.33$  per Month
	
	Pay Using Upi I'd ```lokamandc1224@oksbi```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/mrlokaman")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://www.paypal.me/lokamanchendekar"),
        			InlineKeyboardButton("Paytm",url = "https://p.paytm.me/xCTH/los89jy0")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
