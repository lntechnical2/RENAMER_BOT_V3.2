from pyrogram import Client

import os

from plugins.cb_data import app

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

STRING = os.environ.get("STRING", "")

if STRING:

        bot = Client(

           ":memory:",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,
           in_memory=True,

           plugins=dict(root='plugins'))

        bot.start()

        app.start()

        idle()

else:

	bot = Client( ":memory:",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,
           in_memory=True,

           plugins=dict(root='plugins')) 

	bot.run()
