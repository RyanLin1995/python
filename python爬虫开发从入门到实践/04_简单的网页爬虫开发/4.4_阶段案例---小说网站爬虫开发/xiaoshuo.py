# 从 http://www.kanunu8.com/book3/6879 爬取《动物农场》所有章节的网址,再通过一个多线程爬虫将每一章的内容爬取下来。
# 在本地创建一个“动物农场”文件夹，并将小说中的每一章分别保存到这个文件夹中。每一章保存为一个文件、
import os
import re
from multiprocessing.dummy import Pool

import requests

static_url = "http://www.kanunu8.com/book3/6879"


def get_toc(html):
    """
    获取每一篇文章的链接，存储到一个列表中并返回
    :param html: 目录页源代码
    :return: 每章链接的列表
    """
    toc_url_list = []
    toc_block = re.findall("正文(.*?)</tbody>", html, re.S)[0]
    toc_url = re.findall('href="(.*?)"', toc_block, re.S)
    for url in toc_url:
        toc_url_list.append(static_url + "/" + url)

    return toc_url_list


def get_article(html):
    """
    获取每一章的正文并返回章节名和正文
    :param html: 正文源代码
    :return: 章节名, 正文
    """
    chapter_name = re.search('size="4">(.*?)<', html, re.S).group(1).strip()
    text_block = re.search('<p>(.*?)</p>', html, re.S).group(1)
    text_block = text_block.replace('<br />', '')

    return chapter_name, text_block


def save(chapter, article):
    """
    将每一章保存到本地。
    :param chapter: 章节名, 第X章
    :param article: 正文内容
    :return: None
    """
    os.makedirs('动物农场', exist_ok=True)
    file_name = os.path.join("动物农场", chapter + ".txt")
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(article)


def query_article(url):
    """
    根据正文网址获取正文源代码，并调用 get_article 函数获得正文内容最后保存到本地。
    """
    article_html = requests.get(url).content.decode('gbk')
    chapter, text_block = get_article(article_html)
    save(chapter, text_block)


if __name__ == '__main__':
    toc_html = requests.get(static_url).content.decode('gbk')
    toc_list = get_toc(toc_html)
    pool = Pool(4)
    pool.map(query_article, toc_list)
