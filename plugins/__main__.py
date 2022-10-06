from pyrogram import Client
import os
from plugins.cb_data import app

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")


app = Client(STRING, API_ID, API_HASH)

if STRING:
        bot = Client(
           "renamer",
           bot_token=TOKEN,
           api_id=API_ID,
           api_hash=API_HASH,
           plugins=dict(root='plugins'))
        bot.start()
        app.start()
	idle()
        
        
else:
	bot = Client(
           "renamer",
           bot_token=TOKEN,
           api_id=API_ID,
           api_hash=API_HASH,
           plugins=dict(root='plugins')) 
	bot.run()
