import os
import time
import asyncio
from pyrogram import Client ,filters
from pyrogram.errors import FloodWait
from helper.database import getid ,delete
ADMIN = int(os.environ.get("ADMIN", 923943045))
 

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
    ms = await message.reply_text("Geting All ids from database ...........")
    if (message.reply_to_message):
        try:
            ids = getid()
            tot = len(ids)
            failed = 0 
            success = 0
            startsm = time.time()
            await ms.edit(f"Starting Broadcast .... \n Sending Message To {tot} Users")
            async for id in ids:
                roress = startsm - time.time()
                if (round(roress % 6.00) == 0):
                    try:
                        await ms.edit(text=f"Message sent to {success} chat(s). {failed} chat(s) failed on receiving message. \nTotal - {tot}")
                    except:
                        pass
                try:
     	            await message.reply_to_message.copy(id)
                    success += 1 
                except:
                    try:
     	                failed += 1
     	                delete({"_id":id})
                    except:  	 
     	                pass
        except Exception as e:
            await ms.edit(text=f"ERROR : {e}")
        else:
            await ms.edit(text=f"BROADCST COMPLETED\n\nSUCCESS : {success}\nFAILED : {failed}")
