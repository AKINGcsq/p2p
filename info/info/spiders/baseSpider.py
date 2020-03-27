from scrapy import Request

import scrapy
from info.items import InfoItem
from scrapy.spiders import Spider
import re
import requests
from scrapy import log

from info.items import FailIdItem


class BaseSpider(Spider):
    name = 'base'  # the name of the spider
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.87 Safari/537.36 Edg/80.0.361.48 '
    }
    crawl_number = 60  # the page you want to crawl
    count = 0  # the start page number and the counter
    handle_httpstatus_list = [404, 503]  # the considered http error
    url = 'https://licai.p2peye.com/u'  # the url
    f = []  # the failed page number list



    def start_requests(self):
        start_urls = ['https://licai.p2peye.com/u0/']
        yield Request(start_urls[0], headers=self.headers, dont_filter=True)

    def parse(self, response):
        item = InfoItem()
        failed = FailIdItem()

        if response.status != 200:
            self.f.append(self.count)
            failed['fid'] = self.f

            yield failed
        print(self.f)
        if response.status == 200:

            tzze = response.xpath('/html/body/div[6]/div/section/div[1]/div/div[2]/dl[1]/dd/text()').extract()[
                0]  # 投资总额
            pt = response.xpath('/html/body/div[6]/div/section/div[1]/div/div[2]/dl[2]/dd/text()').extract()[0]  # 投资平台数
            ssd = response.xpath('/html/body/div[6]/div/section/div[1]/div/div[2]/dl[3]/dd/text()').extract()[0]  # 分散度
            syl = response.xpath('/html/body/div[6]/div/section/div[1]/div/div[3]/span/text()').extract()[0]  # 收益率
            item['base'] = [tzze, pt, ssd, syl]

            usr_name = response.xpath('/html/body/div[6]/div/section/div[2]/div[1]/div[1]/div/span/text()').extract()[
                0]  # 用户名

            temp_info = response.xpath('/html/body/div[6]/div/section/div[2]/div[3]/ul/li/span/text()').extract()
            base_info = []
            i = 0
            base_info.append(self.count)
            base_info.append(usr_name)
            while i <= len(temp_info):
                if i % 2 == 1:
                    base_info.append(temp_info[i])
                i += 1
            item['usr_info'] = base_info

            invest_raw = response.xpath('/html/body/div[6]/script/text()').extract()[0]

            dis_pattern = re.compile(r'EchartData_distribution.push\(\{ value:(.*?),name:(.*?)\}\)')
            dis_match = dis_pattern.findall(invest_raw)

            mob_pattern = re.compile(r'EchartData_mobility.push\(\{ value:(.*?),name:(.*?)\}\)')
            mob_match = mob_pattern.findall(invest_raw)

            item['invest_dis'] = dis_match
            item['invest_mob'] = mob_match

            yield item

        self.count += 1
        new_url = self.url + str(self.count) + '/'
        if self.count <= self.crawl_number:
            # print(self.count)
            yield Request(new_url, headers=self.headers, callback=self.parse, dont_filter=True)
