# awesomebook

## 《数据预处理从入门到实战：基于SQL、R、Python》

[日]本桥智光/著   [日]HOXO-M株式会社/审  陈涛/译


## 各语言的预处理执行方法

### SQL的预处理执行

1. 准备AWS Redshift
  - https://aws.amazon.com/jp/redshift/getting-started/
2. 使用SQL Workbench/J连接至Redshift
  - https://docs.aws.amazon.com/ja_jp/redshift/latest/mgmt/connecting-using-workbench.html
3. 准备AWS S3
  - https://aws.amazon.com/jp/s3/
4. 将数据上传至S3
  - 将data文件夹下的csv上传至s3
5. 执行DDL
  - 在preprocess/load_data/ddl目录下的DDL的SQL中设置AWS的键信息并执行
6. 各预处理的执行
  - 执行preprocess文件夹下的预处理代码

### R的预处理执行

1. 下载R
  - https://www.r-project.org/
2. 安装RStudio
  - https://www.rstudio.com/products/rstudio/
3. 启动RStudio
  - 启动已安装的RStudio
4. 设置WorkinkDirectory
  - ```setwd('awesomebook_code的路径')```
5. 安装代码所需的包
  - ```install.packages('包名')```
6. 各预处理的执行
  - 执行preprocess文件夹下的预处理代码


### Python的预处理执行

1. 安装Python3
  - https://www.python.org/
2. 安装PyCharm
  - https://www.jetbrains.com/pycharm/
3. 启动PyCharm動
  - 启动已安装的PyCharm
4. 从终端执行pip命令，安装代码所需的库
  - ```pip3 install 库名```
5. 各预处理的执行
  - 执行preprocess文件夹下的预处理代码


## 目录

- 前言
- 第1部分 预处理入门
----第1章 什么是预处理
- 第2部分 对数据结构的预处理
----第2章 数据提取
----第3章 数据聚合
----第4章 数据连接
----第5章 数据拆分
----第6章 数据生成
----第7章 数据扩展
- 第3部分 对数据结构的预处理
----第8章 数值型
----第9章 分类型
----第10章 日期时间型
----第11章 字符型
----第12章 位置信息型
- 第4部分 预处理实战
----第13章 实战练习

## 支持页面

https://www.ituring.com.cn/book/2650
