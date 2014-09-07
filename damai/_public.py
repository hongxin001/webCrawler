__author__ = 'wei'

import requests
import pymongo, time


conn = pymongo.MongoClient(host='studentunion.vicp.net', port=27017)
db = conn['webcrawler']