# -*- coding: utf-8 -*-
# CreateTime : 2018/3/22 16:34 
# Author : hbzzws

from pymongo import MongoClient

ip = "127.0.0.1"
port = "27017"
logfile = open('mongolog.json', 'w')
try:
    conn = 'mongodb://127.0.0.1:27017/'
    client = MongoClient(conn)

except Exception, e:
    file.write("try conn Error:e:" + e.message)
    print e


class MongoBase:
    def get_db(self, dbname='test'):
        db = client[dbname]
        return db

    def add_one(self, dbName, collectionName, addDict):
        try:
            db = self.get_db(dbName)
            collection = db[collectionName]
            addDict = eval(addDict)
            ret = collection.insert(addDict)
            return ret
        except Exception, e:
            logfile.write("add_one Error:e:" + e.message)
            return False
