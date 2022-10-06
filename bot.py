from pyrogram import Client,idle
import os
import asyncio
from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

STRING = os.environ.get("STRING", "")

if STRING:
	async def main():
	     bots =[Client(":memory:",bot_token=TOKEN,api_id=API_ID,api_hash=API_HASH,plugins=dict(root='plugins')),Client2 ]
	          
	     for bot in bots:
	          await bot.start()
	     await idle()
	     for bot in bots:
	        await bot.stop()
	asyncio.run(main())
	
else:
	bot = Client(":memory:",bot_token=TOKEN,api_id=API_ID,api_hash=API_HASH,plugins=dict(root='plugins'))
	bot.run()	        
