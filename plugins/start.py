import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert ,find_one
from pyrogram.file_id import FileId

from helper.premiumdb import find_one as findpr
from helper.date import add_date ,check_expi
CHANNEL = os.environ.get('CHANNEL',"")
import datetime
STRING = os.environ.get("STRING","")
log_channel = os.environ.get("LOG_CHANNEL","")

#Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
	wish = "Good morning."
elif 12 <= currentTime.hour < 12:
	wish = 'Good afternoon.'
else:
	wish = 'Good evening.'

#-------------------------------

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_text(text =f"""
	Hello {wish} {message.from_user.first_name }
	__I am file renamer bot, Please sent any telegram 
	**Document Or Video** and enter new filename to rename it__
	""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[ InlineKeyboardButton("Support 🇮🇳" ,url="https://t.me/lntechnical") ], 
	[InlineKeyboardButton("Subscribe 🧐", url="https://youtube.com/c/LNtechnical") ]  ]))



@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       update_channel = CHANNEL
       user_id = message.from_user.id
       if update_channel :
       	try:
       		await client.get_chat_member(update_channel, user_id)
       	except UserNotParticipant:
       		await message.reply_text("**__You are not subscribed my channel__** ",
       		reply_to_message_id = message.id,
       		reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("Support 🇮🇳" ,url=f"https://t.me/{update_channel}") ]   ]))
       		return
       
       premi_check  = findpr(user_id)
       
       _used_date = find_one(user_id)
       used_date = _used_date["date"]
       c_time = time.time()
       if premi_check:
           LIMIT = 0
       else:
           LIMIT = 350
       then = used_date+ LIMIT
       left = round(then - c_time)
       conversion = datetime.timedelta(seconds=left)
       ltime = str(conversion)
       if left > 0:
       	    
       	await message.reply_text(f"```Sorry Dude I am not only for YOU \n Flood control is active so please wait for {ltime}```",reply_to_message_id = message.id)
       else:
       		# Forward a single message
       		await client.forward_messages(log_channel, message.from_user.id, message.id)
       		media = await client.get_messages(message.chat.id,message.id)
       		file = media.document or media.video or media.audio 
       		dcid = FileId.decode(file.file_id).dc_id
       		filename = file.file_name
       		value = 2099999999
       		if value < file.file_size:
       		          if STRING:
       		          	try:
       		          		_used_date = findpr(user_id)
       		          		buy_date = _used_date["date"]
       		          		pre_check = check_expi(buy_date)
       		          		if pre_check == True:
       		          			await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {humanize.naturalsize(file.file_size)}\n**Dc ID** :- {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename",callback_data = "rename"),InlineKeyboardButton("✖️ Cancel",callback_data = "cancel")  ]]))
       		          		else:
       		          			await message.reply_text(f'Your Plane Expired On {buy_date}',quote=True)
       		          			
       		          	except Exception as e:
       		          		await message.reply_text(f"You Can't Rename More Then 2GB file\nBuy Subscription\nOur plane\n* Paid Plane ₹ 25  INR For 26days\nPay using Upi ID ```lokamandc1224@oksbi```\nSend Screnshot To @mrlokaman",quote=True)
       		          		return
       		          	
       		          	
       		  
       		          else:
       		          	await message.reply_text("Can't upload files bigger than 2GB ")
       		          return
       		filesize = humanize.naturalsize(file.file_size)
       		fileid = file.file_id
       		await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {filesize}\n**Dc ID** :- {dcid}""",
       		reply_to_message_id = message.id,
       		reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("📝 Rename",callback_data = "rename"),
       		InlineKeyboardButton("✖️ Cancel",callback_data = "cancel")  ]]))
