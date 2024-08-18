import scrapy


class Exercise111Spider(scrapy.Spider):
    name = "exercise11_1"
    allowed_domains = ["exercise.kingname.info"]
    start_urls = ["https://exercise.kingname.info/exercise_xpath_1.html"]

    def parse(self, response):
        name_list = response.xpath(
            '//li[@class="name"]/text()').extract()  # scrapy 中需要用 extract 方法来运行 Xpath。如果不使用 extract，获得的是一个 SelectorList
        price_list = response.xpath('//li[@class="price"]/text()').extract()

        for i in range(len(name_list)):
            print(rf'商品{name_list[i]}，价格为{price_list[i]}')
