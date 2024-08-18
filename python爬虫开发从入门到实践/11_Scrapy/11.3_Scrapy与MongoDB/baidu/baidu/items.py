# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PersonInfoItem(scrapy.Item):  # 定义要爬取的数据
    name = scrapy.Field()
    age = scrapy.Field()
    salary = scrapy.Field()
    phone = scrapy.Field()
