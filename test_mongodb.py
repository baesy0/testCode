#coding:utf8

from pymongo import MongoClient
import datetime 

client = MongoClient("10.10.10.172", 27017)
db = client.projects
projects = "circle"
date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
item = {"name":"김정기",
		"text": "바보",
		"tags":["바보", "쓰레기"],
		"date":date,
}
db[projects].insert_one(item)
