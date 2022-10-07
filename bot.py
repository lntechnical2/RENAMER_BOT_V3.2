import asyncio
from pyrogram import Client, compose
import os

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

STRING = os.environ.get("STRING", "")

app = Client(STRING,API_ID,API_HASH,plugins=dict(root='plugins'))

bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    async def main():
        apps = [app,bot]
        await compose(apps)
    asyncio.run(main())
    
else:
    bot.run()
