from scrapy import Request

import scrapy
from info.items import InfoItem
from scrapy.spiders import Spider
import re


class TestSpider(scrapy.Spider):
    name = 'ip'
    allowed_domains = []

    def parse(self, response):
        print(response.text)

    def start_requests(self):
        url = 'http://ip.chinaz.com/getip.aspx'

        for i in range(4):
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)
