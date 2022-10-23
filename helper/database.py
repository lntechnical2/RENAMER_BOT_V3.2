import pymongo 
import os
from helper.date import add_date
DB_NAME = os.environ.get("DB_NAME","")
DB_URL = os.environ.get("DB_URL","")
mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["user"]

def insert(chat_id):
            user_id = int(chat_id)
            user_det = {"_id":user_id,"file_id":None ,"daily":0 ,"date":0 , "uploadlimit" :2147483648,"used_limit":0,"usertype":"Free","prexdate" : None}
            try:
            	dbcol.insert_one(user_det)
            except:
            	pass

def addthumb(chat_id, file_id):
	dbcol.update_one({"_id":chat_id},{"$set":{"file_id":file_id}})
	
def delthumb(chat_id):
	dbcol.update_one({"_id":chat_id},{"$set":{"file_id":None}})
	
def dateupdate(chat_id,date):
	dbcol.update_one({"_id":chat_id},{"$set":{"date":date}})

def used_limit(chat_id,used):
	dbcol.update_one({"_id":chat_id},{"$set":{"used_limit":used}})
	
def usertype(chat_id,type):
	dbcol.update_one({"_id":chat_id},{"$set":{"usertype":type}})
	
def uploadlimit(chat_id,limit):
	dbcol.update_one({"_id":chat_id},{"$set":{"uploadlimit":limit}})

def addpre(chat_id):
    date = add_date()
    dbcol.update_one({"_id":chat_id},{"$set":{"prexdate":date[0]}})

def addpredata(chat_id):
    dbcol.update_one({"_id":chat_id},{"$set":{"prexdate":None}})
    
  
def daily(chat_id,date):
	  dbcol.update_one({"_id":chat_id},{"$set":{"daily":date}})
	  
def find(chat_id):
	id =  {"_id":chat_id}
	x = dbcol.find(id)
	for i in x:
             file = i["file_id"]
             return file

def getid():
    values = []
    for key  in dbcol.find():
         id = key["_id"]
         values.append((id)) 
    return values

def delete(id):
	dbcol.delete_one(id)
	
def find_one(id):
	return dbcol.find_one({"_id":id})
