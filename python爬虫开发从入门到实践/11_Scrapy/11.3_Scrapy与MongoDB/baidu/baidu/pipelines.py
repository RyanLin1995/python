# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from baidu import settings
import pymongo


class BaiduPipeline:

    def __init__(self):  # pipeline 中初始化 MONGODB
        host = settings.MONGODB_HOST
        port = settings.MONGODB_PORT
        db_name = settings.MONGODB_DBNAME
        client = pymongo.MongoClient(host=host, port=port)
        db = client[db_name]
        self.post = db[settings.MONGODB_DOCNAME]

    def process_item(self, item, spider):  # 爬取数据后将数据保存到 MONGODB 中
        person_info = dict(item)
        self.post.insert_one(person_info)
        return item
