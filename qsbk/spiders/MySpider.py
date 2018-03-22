# -*- coding: utf-8 -*-
# CreateTime : 2018/3/22 16:33 
# Author : hbzzws

import scrapy
# 引入容器
from qsbk.items import Item


class MySpider(scrapy.Spider):
    # 设置name
    name = "MySpider"
    # 设定域名
    allowed_domains = ["qiushibaike.com"]
    # 填写爬取地址
    qiushibaikedomain = "https://www.qiushibaike.com"
    start_urls = [qiushibaikedomain + "/text/page/1/"]

    # 编写爬取方法
    def parse(self, response):
        # 实例一个容器保存爬取的信息
        item = Item()
        # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        for box in response.xpath('//div[@id="content-left"]/div'):
            item['content'] = "".join(box.xpath('.//div[@class="content"]/span/text()').extract())
            item['author_name'] = box.xpath('.//img[1]/@alt').extract()[0].strip()
            item['author_img'] = box.xpath('.//img[1]/@src').extract()[0].strip()
            niming = u"匿名用户"
            if item["author_name"] == niming:
                item['author_gender'] = "unkonw"
                item['author_age'] = "0"
            else:
                item['author_gender'] = box.xpath('./div[1]/div/@class').extract()[0].split(" ")[1][:-4]
                item['author_age'] = box.xpath('./div[1]/div/text()').extract()[0]
            item['zancount'] = box.xpath('.//i[@class="number"]/text()').extract()[0].strip()
            item['commentcount'] = box.xpath('.//i[@class="number"]/text()').extract()[1].strip()
            # 返回信息
            yield item
        pagetext = response.xpath("//ul[@class='pagination']/li[last()]//span/text()").extract()[0].strip()
        pageurl = response.xpath("//ul[@class='pagination']/li[last()]//a/@href").extract()[0].strip()
        netxtpage = u"下一页"
        if pagetext == netxtpage:
            yield scrapy.Request(self.qiushibaikedomain + pageurl, callback=self.parse)
