import requests
import redis
import lxml.html

base_url = "https://www.ziwushuwu.com/dongyeguiwuzuopinji/5525/"
r = redis.StrictRedis()

response = requests.get(base_url).content.decode('utf-8')
selector = lxml.html.fromstring(response)
url_list = selector.xpath('//ul[@class="readers-list"]/li/a/@href')
for url in url_list:
    r.lpush('url_queue', base_url + url)
