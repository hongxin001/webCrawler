# coding=utf-8
__author__ = 'wei'
import requests
import pymongo, time
from tools import timestamp

conn = pymongo.MongoClient(host='studentunion.vicp.net', port=27017)
db = conn['webcrawler']
url = "http://studentunion.vicp.net:808/event/create"

tables = db.zhiboba.find()

for table in tables:
    if table["Is"]=="0" :
        time = timestamp.timestamp_datetime(table["Time"])
        content = table["Title"]+" "+time+" "+table["Address"]
        title = table["Title"]
        data = { "title" : title , "content" : title , "privacy" : 1 , "addr" : table['Address'] , "alarm.starttime" : table['Time'] , "alarm.period" : 0 , "alarm.earlier" : 0, "access_token" : "53e0abd91d41c8322d14d7c3.1440847878.561233b565a7e9da4df80eec415faf60"}
        r = requests.post(url,data)
        if r.ok:
            print r.json()
        print table["Title"]
        print table["Address"]
        print " "