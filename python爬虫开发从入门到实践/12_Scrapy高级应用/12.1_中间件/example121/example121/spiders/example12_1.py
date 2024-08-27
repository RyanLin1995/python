import scrapy


class Example121Spider(scrapy.Spider):
    name = "example12_1"
    allowed_domains = ["exercise.kingname.info"]
    start_urls = ["https://exercise.kingname.info/exercise_middleware_ip",
                  "https://exercise.kingname.info/exercise_middleware_ip/2",
                  "https://exercise.kingname.info/exercise_middleware_ip/3"]

    def parse(self, response):
        print(response.body.decode())
