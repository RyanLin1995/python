# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Example121Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ErrorItem(scrapy.Item):
    page = scrapy.Field()
    error_time = scrapy.Field()
