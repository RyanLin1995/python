from scrapy_redis.spiders import RedisSpider  # 导入 Redis Spider
from example114.items import PersonInfoItem


class Example114Spider(RedisSpider):
    name = "example11_4"
    redis_key = "example_redis_spider:start_url"  # 这里的 redis_key 实际上就是一个变量名，之后爬虫爬到的所有 URL 都会保存到 Redis 中这个列表下面，
    # 爬虫同时也会从这个列表中读取后续页面的 URL。这个变量名可以任意修改，里面的英文冒号也不是必需的。
    # 不过一般习惯上会写成“爬虫名:start uls”这种形式，这样看到名字就可知道保存的是什么内容了。

    # 因为上边添加了 redis_key 所以下边的链接信息不生效了，爬虫只会从 example_redis_spider:start_url 列表中读取 url。
    # 可以使用 lpush example_redis_spider:start_url https://exercise.kingname.info/exercise_xpath_3.html 给列表添加 URL，但 scrapy_redis 推荐在列表中插入 JSON
    allowed_domains = ["exercise.kingname.info"]
    start_urls = ["https://exercise.kingname.info/exercise_xpath_3.html"]

    def parse(self, response):
        person_list = response.xpath('//div[@class="person_table"]/table/tbody/tr')
        for person in person_list:
            item = PersonInfoItem()
            person_info = person.xpath('td/text()').extract()
            item['name'] = person_info[0]
            item['age'] = person_info[1]
            item['salary'] = person_info[2]
            item['phone'] = person_info[3]
            yield item  # yield 是将存放好的数据交给 pipeline 处理
