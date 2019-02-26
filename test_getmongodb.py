#coding:utf8
from pymongo import MongoClient
import datetime

client = MongoClient("10.10.10.172", 27017)
db = client.projects
project = "circle"

date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

item = db[project].find_one({"name":"sunyong"})
item["text"] = "new text"
item["date"] = date
db[project].update_one({"name":"sunyong"}, {"$set":item}, upsert = False)

