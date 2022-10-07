import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    async def main():
        apps = [app,bot]
        
        for app in apps:
            await app.start()
        await idle()
        for app in apps:
            await app.stop()
    asyncio.run(main())
    
else:
    bot.run()
