### 1. 创建项目
```commandline
scrapy startproject <工程名>
```
PS:
- 工程名不能是 Python 包名

### 2. 创建爬虫
```commandline
scrapy genspider <爬虫名字> <需要爬取的网址>
```
PS:
- 爬虫名字不能跟工程名字重名。例如这里工程名字是 baidu，所以爬虫名字不能是 baidu


### 3. 启动爬虫
```commandline
cd <工程根目录>
scrapy crawl <爬虫名字>
```
PS:
- Scrapy 可能遵守 robots.txt 而不去进行爬虫，需要做一点修改
  ```python
  # 在工程文件夹下找到 settings.py，修改以下为 False
  # Obey robots.txt rules
  ROBOTSTXT_OBEY = False
  ```

### 4. 文件结构
- spiders 文件夹：存放爬虫文件的文件夹
- items.py：定义需要抓取的数据
- pipelines.py：负责数据抓取以后的处理工作
- setting.py：爬虫的各种配置信息