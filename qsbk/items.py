# -*- coding: utf-8 -*-
# CreateTime : 2018/3/22 16:29 
# Author : hbzzws

# 引入文件
import scrapy


class Item(scrapy.Item):
    # 内容
    content = scrapy.Field()
    # 作者
    author_name = scrapy.Field()
    # 用户头像
    author_img = scrapy.Field()
    # 性别
    author_gender = scrapy.Field()
    # 年龄
    author_age = scrapy.Field()
    # 点赞人数
    zancount = scrapy.Field()
    # 评论人数
    commentcount = scrapy.Field()
