import json
import re

import requests

base_url = "https://www.le.com/ptv/vplay/1578861.html"


class LetvSipder:
    HEADER = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
        "Connection": "keep-alive",
        "Cookie": "tj_lc=a3dfcf5e926207506b878344dacc4d56; tj_uuid=-_17227414221181630955; tj_env=1; language=zh-cn; bd_xid=a3dfcf5e926207506b878344dacc4d56; sso_curr_country=CN; currentTop_miniPlayer=666; currentLeft_miniPlayer=826; tj_v2c=-934961_2-1578861_2-77573421_1009; ark_uuid=ck-4638d3e7-efde-4b57-b64f-214e9c5e191f-0804-120857",
        "Host": "api-my.le.com",
        "Referer": "https://www.le.com/",
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua": "Not/A)Brand;v=8, Chromium;v=126, Google Chrome;v=126",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows"
    }

    COMMENT_URL = "https://api-my.le.com/vcm/api/list?type=video&rows=100&page=1&sort=&cid=2&source=1&xid={xid}&pid={pid}&ctype=cmt%2Cimg%2Cvote&listType=1"  # listType 0 是弹幕，1 是评论

    def __init__(self, url):
        self.base_url = url
        self.necessary_info = {}
        self.get_necessary_id()
        self.get_comment()

    @staticmethod
    def get_source(url, headers):
        return requests.get(url, headers).content.decode()

    def get_necessary_id(self):
        source = self.get_source(self.base_url, self.HEADER)
        vid = re.search(r'vid: (\d+)', source).group(1)
        pid = re.search(r'pid: (\d+)', source).group(1)
        self.necessary_info['xid'] = vid.strip()
        self.necessary_info['pid'] = pid.strip()

    def get_comment(self):
        url = self.COMMENT_URL.format_map(self.necessary_info)
        source_data = requests.get(url, self.HEADER).json()['data']
        for comment in source_data:
            print(rf"发帖人：{comment['user']['username']}, 评论内容：{comment['content']}")


if __name__ == '__main__':
    le_spider = LetvSipder(base_url)
