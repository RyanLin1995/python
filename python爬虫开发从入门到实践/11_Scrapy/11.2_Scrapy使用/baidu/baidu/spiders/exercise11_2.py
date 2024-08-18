import scrapy


class Exercise112Spider(scrapy.Spider):
    name = "exercise11_2"
    allowed_domains = ["exercise.kingname.info"]
    start_urls = ["https://exercise.kingname.info/exercise_xpath_2.html"]

    def parse(self, response):
        # 先抓大的，再抓小的
        items_list = response.xpath('//ul[@class="item"]')  # 这里抓的是大的范围，所以先不需要 extract
        for item in items_list:
            name = item.xpath('li[@class="name"]/text()').extract()
            price = item.xpath('li[@class="price"]/text()').extract()
            name = name[0] if name else "N/A"
            price = price[0] if price else "N/A"
            print(rf'商品{name}，价格为{price}')
