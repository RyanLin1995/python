# 需求：在百度贴吧中任意寻找一个贴吧并打开一个热门帖子，将帖子源码复制下来，保存为 source.txt、通过读取这个 source.txt，
# 使用正则表达式获取用户名、发帖内容和发帖时间，并保存到 result.csv
import csv
import re

with open('source.txt', encoding='utf-8') as file:
    source = file.read()

result_list = []
# 先获得每一层楼所有信息的大文本块
every_reply = re.findall('l_post l_post_bright j_l_post clearfix (.*?)p_props_tail props_appraise_wrap', source, re.S)

for each in every_reply:
    result = {'username': re.findall('username="(.*?)"', each, re.S)[0],
              'content': re.findall('class="d_post_content j_d_post_content " style="display:;">(.*?)<', each,
                                    re.S)[0].strip(),
              'reply_time': re.findall(r'class="tail-info">(\d{4}.*?)<', each, re.S)[0]}
    result_list.append(result)

with open('result.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['username', 'content', 'reply_time'])
    writer.writeheader()
    writer.writerows(result_list)
