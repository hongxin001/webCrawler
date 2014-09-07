# coding=utf-8
import requests
import pymongo
import time
from bs4 import BeautifulSoup
from tools import timestamp

__author__ = 'wei'

conn = pymongo.MongoClient(host='studentunion.vicp.net', port=27017)
db = conn['webcrawler']

url = "http://www.zhibo8.cc/"
content = requests.get(url)
content = content.content.decode('utf-8')
soup = BeautifulSoup(content)

year = time.strftime("%Y", time.localtime(time.time()))
boxs = soup.find(id="left").findAll(attrs={'class': 'box'})

for box in boxs:
    date = box.contents[1].h2.string
    lis = box.find(attrs={'class': 'content'}).ul.findAll("li")
    for li in lis:
        b = li.find("b")
        if b is None:
            continue;
        else:

            s = li.text
            time = year + "-" + date[0:2] + "-" + date[3:5] + " " + s[0:5] + ":00"
            time = timestamp.datetime_timestamp(time);
            place = li.find("a").text
            c = b.text

            print("\n")
            if (db.zhiboba.find_one({"Title": c}, None) == None):
                print(time)
                print(place)
                print(b.text)
                item = {"Title": c, "Address": place, "Time": time,"Is":"0"}
                db.zhiboba.save(item)
