#coding:utf8
import redis

r = redis.Redis(
	host = '10.10.10.172',
	port=6379)

print r.get("kimhanwoong")
r.set("kimjeonggi","fool")
print r.get("kimjunggi")
print r.get("kwondoyoung")
