# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from example121.items import ErrorItem
from example121 import settings


class Example121Pipeline:

    def __init__(self):
        self.db = pymongo.MongoClient(host=settings.MONGODB_HOST, port=settings.MONGODB_PORT)[settings.MONGODB_DB]
        self.handler = None

    def process_item(self, item, spider):
        if isinstance(item, ErrorItem):
            self.process_error(item)
        return item

    def process_error(self, item):
        if not self.handler:
            self.handler = self.db[settings.MONGODB_ERROR]
        self.handler.insert_one(dict(item))
