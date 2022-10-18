from PIL import Image
import time
from urllib.request import urlretrieve
from urllib import request
import math
import time
from pyrogram import Client , filters
import os 
import requests
from function.progress import progress_for_pyrogram ,humanbytes ,TimeFormatter
from function.database import find
from hachoir.metadata import extractMetadata 
from hachoir.parser import createParser

from function.premiumdb import find_one as findpr
from function.date import add_date ,check_expi

app = Client("test", api_id=1022247, api_hash='fdaeeb8d0c120cab6385646849dc2868', session_string="BQAPmScApLeUrPnZX5dG9eyvJuFiX9-6FY32w51q80ufCGAPBGk0oxrT3sS4n7tEy-EztdEjHA2rtzYITgEHWvLqZYKC0Hnt6ScffvczcYrcBKA69BNxsMjmQJHTYyL7J5OGaZahbPf1PyMOThAyTlX8L6zxFusnIJjGaUsl6xdUUdGAmd51w1oNEU87RNEwy9cqcOnZeJzAfzd0Cnga-8kd40xFd2dp74skE2_9Y9N6NA0eDMvdb66fREgvc8NCJQLi25zX5jTrPiJXkak74eeOa4l_2aMfxLJRDHMNEFzflvxCxQ5ZsO65Hik6lPHxBr5eGMv4iByJO5SW5GHf0eJhyOUa8AAAAAA3EkCFAA")


@Client.on_callback_query(filters.regex('doc'))
async def doc(bot,update):
	url = update.message.reply_to_message.text
	web = request.urlopen(url)
	data = web.info()
	file_size = data.get('Content-Length')
	value = 2099999999
	if value < int(file_size):
	    try:
	        _used_date = findpr(update.from_user.id)
	        buy_date = _used_date["date"]
	        pre_check = check_expi(buy_date)
	        if pre_check == True:
	            await update.message.edit("Downloading.......")
	        else:
	                await update.message.edit(f'Your Plane Expired On {buy_date}')
        	        return
	    except Exception as e:
        	    await update.message.edit(f"You can't Upload More Then 2GB File {e} ")
        	    return
	file_name = data.get_filename()
	start = time.time()
	display_message = ""
	CHUNK = 1024
	await update.message.edit("Downloading....... 🖥️")
	r = requests.get(url, allow_redirects=True, stream=True)
	total_size = int(r.headers.get("content-length", 0))
	downloaded = 0
	with open(file_name, 'wb') as fd:
	           for chunk in r.iter_content(chunk_size=CHUNK):
	               if chunk:
	               	fd.write(chunk)
	               	downloaded += CHUNK	
	               	now = time.time()
	               	diff = now - start
	               	if round(diff % 5.0) == 0 or downloaded == total_size:
	               	   percentage = int(downloaded) * 100 / int(total_size)
	               	   speed = int(downloaded) / diff
	               	   elapsed_time = round(diff) * 1000
	               	   time_to_completion = (round(int(total_size - downloaded) / speed) * 1000)
	               	   estimated_total_time =TimeFormatter(elapsed_time + time_to_completion)
	               	   progress = "[{0}{1}] \n**Progress**: {2}%\n".format(''.join(["●" for i in range(math.floor(percentage / 5))]),''.join(["○" for i in range(20 - math.floor(percentage / 5))]),round(percentage, 2))
	               	   tmp = progress + "{0} of {1}\n**Speed**: {2}/s\n**ETA**: {3}\n".format(humanbytes(downloaded),humanbytes(total_size),humanbytes(speed),estimated_total_time if estimated_total_time != '' else "0 s")
            
	               	   try:
	               	       current_message = tmp
	               	       
	               	       if current_message != display_message:
	               	           await update.message.edit(current_message)
	               	           display_message = current_message
	               	   except Exception as e:
	               	   	await update.message.edit(e)
	thumb = find(update.from_user.id)
	if thumb:
	      ph_path = await bot.download_media(thumb)
	      Image.open(ph_path).convert("RGB").save(ph_path)
	      img = Image.open(ph_path)
	      img.resize((320, 320))
	      img.save(ph_path, "JPEG")
	      thumbnail = ph_path
	else:
	     thumbnail = None
	ms = await update.message.edit("Uploading............")
	c_time = time.time()
	if value < int(file_size):
	    filw = await app.send_document(-1001750197277,file_name,thumb =thumbnail,progress=progress_for_pyrogram,progress_args=( "```Trying To Uploading```",  ms, c_time   ))
	    from_chat = filw.chat.id
	    mg_id = filw.id
	    await bot.copy_message(update.from_user.id,from_chat,mg_id)
	    await ms.delete()
	    os.remove(file_name)
	else:
	   await bot.send_document(update.from_user.id,file_name,thumb =thumbnail,progress=progress_for_pyrogram,progress_args=( "```Trying To Uploading```",  ms, c_time   ))
	   await ms.delete()
	   os.remove(file_name)
	
@Client.on_callback_query(filters.regex('vid'))
async def vid(bot,update):
	url = update.message.reply_to_message.text
	web = request.urlopen(url)
	data = web.info()
	file_size = data.get('Content-Length')
	value = 2099999999
	if value < int(file_size):
	    try:
	        _used_date = findpr(update.from_user.id)
	        buy_date = _used_date["date"]
	        pre_check = check_expi(buy_date)
	        if pre_check == True:
	            await update.message.edit("Downloading.......")
	        else:
	                await update.message.edit(f'Your Plane Expired On {buy_date}')
        	        return
	    except Exception as e:
        	    await update.message.edit(f"You can't Upload More Then 2GB File {e} ")
        	    return
	file_name = data.get_filename()
	start = time.time()
	display_message = ""
	CHUNK = 1024
	await update.message.edit("Downloading....... 🖥️")
	r = requests.get(url, allow_redirects=True, stream=True)
	total_size = int(r.headers.get("content-length", 0))
	downloaded = 0
	with open(file_name, 'wb') as fd:
	           for chunk in r.iter_content(chunk_size=CHUNK):
	               if chunk:
	               	fd.write(chunk)
	               	downloaded += CHUNK	
	               	now = time.time()
	               	diff = now - start
	               	if round(diff % 5.0) == 0 or downloaded == total_size:
	               	   percentage = int(downloaded) * 100 / int(total_size)
	               	   speed = int(downloaded) / diff
	               	   elapsed_time = round(diff) * 1000
	               	   time_to_completion = (round(int(total_size - downloaded) / speed) * 1000)
	               	   estimated_total_time =TimeFormatter(elapsed_time + time_to_completion)
	               	   progress = "[{0}{1}] \n**Progress**: {2}%\n".format(''.join(["●" for i in range(math.floor(percentage / 5))]),''.join(["○" for i in range(20 - math.floor(percentage / 5))]),round(percentage, 2))
	               	   tmp = progress + "{0} of {1}\n**Speed**: {2}/s\n**ETA**: {3}\n".format(humanbytes(downloaded),humanbytes(total_size),humanbytes(speed),estimated_total_time if estimated_total_time != '' else "0 s")
            
	               	   try:
	               	       current_message = tmp
	               	       
	               	       if current_message != display_message:
	               	           await update.message.edit(current_message)
	               	           display_message = current_message
	               	   except Exception as e:
	               	   	await update.message.edit(e)
	thumb = find(update.from_user.id)
	if thumb:
	      ph_path = await bot.download_media(thumb)
	      Image.open(ph_path).convert("RGB").save(ph_path)
	      img = Image.open(ph_path)
	      img.resize((320, 320))
	      img.save(ph_path, "JPEG")
	      thumbnail = ph_path
	else:
	     thumbnail = None
	ms = await update.message.edit("Uploading............")
	c_time = time.time()
	duration = 0
	metadata = extractMetadata(createParser(file_name))
	if metadata.has("duration"):
		duration = metadata.get('duration').seconds  
	if value < int(file_size):
	    filw = await app.send_document(-1001750197277,file_name,thumb =thumbnail,progress=progress_for_pyrogram,progress_args=( "```Trying To Uploading```",  ms, c_time   ))
	    from_chat = filw.chat.id
	    mg_id = filw.id
	    await bot.copy_message(update.from_user.id,from_chat,mg_id)
	    await ms.delete()
	    os.remove(file_name)
	else:
	   await bot.send_video(update.from_user.id,file_name,thumb =thumbnail,duration =duration,progress=progress_for_pyrogram,progress_args=( "```Trying To Uploading```",  ms, c_time   ))
	   await ms.delete()
	   os.remove(file_name)
