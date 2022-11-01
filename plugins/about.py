import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"Bot :- @rename_urbot\nCreater :- @mrlokaman\nLanguage :-Python3\nLibrary :- Pyrogram 2.0\nServer :- Railway\nTotal Renamed File :-{total_rename}\nTotal Size Renamed :- {humanbytes(total_size)} ",quote=True)
