# coding=utf-8
import requests
import pymongo, time
from tools import timestamp
from bs4 import BeautifulSoup


__author__ = 'wei'

furl = "http://www.damai.cn/projectlist.do?mcid=1"
r = requests.get(furl)
r = r.content.decode('utf-8')

soup = BeautifulSoup(r)
list = soup.find(id="performList").findAll("li")

conn = pymongo.MongoClient(host='studentunion.vicp.net', port=27017)
db = conn['webcrawler']
str = "状态: 销售中"

for li in list:
    text = li.find(attrs={"class": "ri-infos"}).findAll("p")
    if text[3].text == str.decode("utf-8"):
        line = li.find(attrs={"class": "img"}).find("a")
        href = line['href']
        r2 = requests.get(href)
        cont = r2.content.decode('utf-8')
        s2 = BeautifulSoup(cont)
        title = s2.find(attrs={"class": "title"}).h1.text
        img = s2.find(attrs={"class": "goods-basic-poster"}).find("img")
        address = s2.find(attrs={"class": "mr15"}).a
        address = address["title"]

        time = s2.find(attrs={"class": "b-select-date b-perform-times b-one-date"}).dd.a.text
        time = time[0:10] + " " + time[15:20] + ":00"
        time = timestamp.datetime_timestamp(time);

        imgurl = img["original"]
        print(title)
        print(address)
        print(time)
        print(imgurl)
        print("\n")
        if (db.damai.find_one({"Title": title}, None) == None ):
            item = {"Title": title, "Address": address, "Time": time, "imaurl": imgurl}
            db.damai.save(item)
