# -*- coding: utf-8 -*-
# CreateTime : 2018/3/22 16:29 
# Author : hbzzws



# 引入文件
from qsbk.mongo.base import MongoBase
import json


class MyPipeline(object):
    def __init__(self):
        # 打开文件
        self.db = MongoBase()
        # self.file = open('data.json', 'w')

    # 该方法用于处理数据
    def process_item(self, item, spider):
        # self.file.write("\n process".encode("utf-8"))
        # 读取item中的数据
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # 写入文件
        # content = json.dumps(dict(item)["content"], ensure_ascii=False).strip()
        # self.file.write(content.encode("utf-8"))
        self.db.add_one("pachong1", "qiushibaike", line.encode("utf-8"))

        # 返回item
        return item

    # 该方法在spider被开启时被调用。
    def open_spider(self, spider):
        # self.file.write("###########open############\n")
        pass


# 该方法在spider被关闭时被调用。
def close_spider(self, spider):
    # self.file.write("\n###########close############")
    # self.file.close()
    pass
