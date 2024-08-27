import datetime
import json
from typing import Iterable

import scrapy
from scrapy import Request


class Example1212Spider(scrapy.Spider):
    name = "example12_1_2"
    allowed_domains = ["exercise.kingname.info"]
    start_urls = ["https://exercise.kingname.info/exercise_middleware_retry_backend/para/{}"]

    def start_requests(self) -> Iterable[Request]:
        for i in range(1, 11):
            url = self.start_urls[0].format(i)
            if i == 5:
                request_body = json.dumps({'date': str(datetime.date.today() - datetime.timedelta(days=1))})
            else:
                request_body = json.dumps({'date': str(datetime.date.today())})
            yield scrapy.Request(url, method='POST', body=request_body, headers={'content-type': 'application/json'},
                                 meta={'page': i})

    def parse(self, response):
        if '参数错误' in response.body.decode():
            raise Exception('参数错误')
        else:
            print(response.body.decode())
