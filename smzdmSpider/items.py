# -*- coding: utf-8 -*-

# 数据模型示意已经放在了Design文件夹下

import scrapy

class ZongHeItems(scrapy.Item):
    tag = scrapy.Field()
    image = scrapy.Field()
    title = scrapy.Field()
    discounts = scrapy.Field()
    description = scrapy.Field()
    goods = scrapy.Field()
    bads = scrapy.Field()
    stars = scrapy.Field()
    comments = scrapy.Field()
    time = scrapy.Field()
    provider = scrapy.Field()
    purchase_link = scrapy.Field()

class HotSearchItem(scrapy.Item):
    name = scrapy.Field()
    href = scrapy.Field()


class Tags(scrapy.Item):
    name = scrapy.Field()
    href = scrapy.Field()


class SmzdmspiderItem(HotSearchItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

