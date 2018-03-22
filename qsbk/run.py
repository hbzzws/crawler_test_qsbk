# -*- coding: utf-8 -*-
# CreateTime : 2018/3/22 16:29 
# Author : hbzzws


import urllib2

from scrapy import cmdline

name = 'MySpider'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
