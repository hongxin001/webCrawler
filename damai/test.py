import HTMLParser

__author__ = 'wei'
import urllib
from BeautifulSoup import BeautifulSoup

furl = "http://item.damai.cn/66780.html"
content = urllib.urlopen(furl).read()

# soup = BeautifulSoup(content)

hp = HTMLParser.HTMLParser();
# s = hp.unescape(soup)
print content