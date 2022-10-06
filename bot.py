from pyrogram import Client
import os
from plugins.cb_data import app
TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    bot = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    bot.start()
    app.start()
    idle()
