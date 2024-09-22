import scrapy
from scrapy_redis.spiders import RedisSpider
from lxml import etree
from html import unescape

from example115.items import Example115Item


class Example115Spider(RedisSpider):
    name = "example_115"
    allowed_domains = ["www.kingname.info", "kingname.info"]
    redis_key = 'blogspider'
    # start_urls = ["https://kingname.info/archives/"]
    start_urls = ["https://kingname.info/2024/07/28/nature-crawl/"]
    host = 'https://kingname.info'

    def parse(self, response):
        title_tag_list = response.xpath('//a[@class="post-title-link"]')
        for title_tag in title_tag_list:
            article_title = title_tag.xpath('span/text()').extract_first()
            article_url = self.host + title_tag.xpath('@href').extract_first()
            item = Example115Item()
            item['title'] = article_title
            item['url'] = article_url
            yield scrapy.Request(article_url,
                                 method="get",
                                 headers=self.settings['HEADERS'],  # 一定要注意 header 的 encoding 不可以是 gzip
                                 callback=self.parse_detail,
                                 meta={'item': item})

    def parse_detail(self, response):
        item = response.meta['item']  # 从 meta 取数据。由于上面定义了 meta={'item': item}，所以这里通过 item 读取
        post_time = response.xpath('//span[@class="post-meta-item"]/time/@datetime').extract_first()
        category = ','.join(
            [i.extract().replace('# ', '') for i in response.xpath('//div[@class="post-tags"]/a/text()') if
             i])
        post_body = unescape(etree.tostring(response.xpath('//div[@itemprop="articleBody"]')[0].root).decode())
        item['post_time'] = post_time
        item['category'] = category
        item['detail'] = post_body
        yield item
