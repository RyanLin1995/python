import redis
import requests
import lxml.html
from pymongo import MongoClient

r = redis.StrictRedis()
m_client = MongoClient()
m_database = m_client['test']
m_collection = m_database['baiyexing']

m_insert_data = []

while r.llen('url_queue') > 0:
    url = r.lpop('url_queue').decode()
    response = requests.get(url).content.decode('utf-8')
    selector = lxml.html.fromstring(response)
    title = selector.xpath('//div[@class="maike"]/h1/text()')[0]
    content = ''
    content_data = selector.xpath('//div[@class="maike"]/p[@class="p"]')
    for content_xpath in content_data[2:-3]:
        content += str(content_xpath.xpath('string(.)')).strip() + "\n"
    m_insert_data.append({'title': title, 'content': content})

m_collection.insert_many(m_insert_data)
