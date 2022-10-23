import time
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from helper.database import  find_one 
import datetime
from datetime import timedelta, date ,datetime
from helper.progress import humanbytes


@Client.on_message(filters.private & filters.command(["myplan"]))
async def start(client,message):
	used_ = find_one(message.from_user.id)
	used = used_["used_limit"]
	limit = used_["uploadlimit"]
	remain = int(limit)- int(used)
	user =  used_["usertype"]
	ends = used_["prexdate"]
	normal_date = datetime.fromtimestamp(ends).strftime('%Y-%m-%d')
	if ends ==0:
	    text = f"User ID:- ```{message.from_user.id}```\nPlan :- {user}\nDaly Upload Limit :- {humanbytes(limit)}\nToday Used :- {humanbytes(used)}\nRemain:- {humanbytes(remain)}"
	else:
	    text = f"User ID:- ```{message.from_user.id}```\nPlan :- {user}\nDaly Upload Limit :- {humanbytes(limit)}\nToday Used :- {humanbytes(used)}\nRemain:- {humanbytes(remain)}\n\n```Your Plan Ends On :- {normal_date}"
	    
	if user == "Free":
	    await message.reply(text,quote = True,reply_markup = InlineKeyboardMarkup([[       			InlineKeyboardButton("Upgrade 💰💳",callback_data = "upgrade"), InlineKeyboardButton("Cancel ✖️ ",callback_data = "cancel") ]]))
	else:
	    await message.reply(text,quote=True)
	    
