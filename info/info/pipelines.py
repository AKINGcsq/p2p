# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from info.items import InfoItem, FailIdItem


class InfoPipeline(object):
    def __init__(self):
        self.file = codecs.open('baseInfo.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        if isinstance(item, InfoItem):
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file.write(line)
            return item

    def spider_closed(self, spider):
        self.file.close()


class FailPipeline(object):
    def __init__(self):
        self.file = codecs.open('fid.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        if isinstance(item, FailIdItem):
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file.write(line)
            return item

    def spider_closed(self, spider):
        self.file.close()


class TestPipeline(object):
    def __init__(self):
        self.file1 = codecs.open('info.json', 'a', encoding='utf-8')

        self.file2 = codecs.open('fid.json', 'w', encoding='utf-8')


    def process_item(self, item, spider):
        if isinstance(item, FailIdItem):
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file2.write(line)
            return item
        elif isinstance(item, InfoItem):
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file1.write(line)
            return item

    def spider_closed(self, spider):
        self.file2.close()
        self.file1.close()
