# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class InfoItem(scrapy.Item):
    base = scrapy.Field()
    invest_dis = scrapy.Field()
    invest_mob = scrapy.Field()
    usr_info = scrapy.Field()


class FailIdItem(scrapy.Item):
    fid = scrapy.Field()
