# 浏览器向服务器发送的请求格式如下:
# 【数据来自127.0.0.1:41206】
# GET / HTTP/1.1  # 表示浏览器请求什么，如果只是域名的话，get 后面只会显示 /；如果是域名/index.html等页面，get 后面会显示请求的页面，如index.html
# Host: 127.0.0.1:8081  #  请求目标的IP即端口
# Connection: keep-alive  # 长连接
# Cache-Control: max-age=0
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36  # 浏览器版本
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9  # 浏览器可以接收的格式
# Sec-Fetch-Site: none
# Sec-Fetch-Mode: navigate
# Sec-Fetch-User: ?1
# Sec-Fetch-Dest: document
# Accept-Encoding: gzip, deflate, br  # 浏览器支持的压缩方式
# Accept-Language: zh-CN,zh;q=0.9,en;q=0.8  # 浏览器支持的语言
# Cookie: csrftoken=pg7Y87dyJgV1w6pjym1qzcze5YB9eV1rJST20W2Yi86jpQ5nPDRPJfazJmK3OKI1

# 服务器给浏览器回送的数据格式如下:
# 1. Header
# HTTP/1.1 200 OK  # 如果服务器找到浏览器请求的页面，则返回200
# Bdpagetype: 2
# Bdqid: 0xc22cc1ce000019ab
# Cache-Control: private  # 缓存类型: 私有
# Connection: keep-alive
# Content-Encoding: gzip  # 服务器压缩格式
# Content-Type: text/html;charset=utf-8  # 服务器的格式和编码
# Date: Thu, 01 Oct 2020 08:23:36 GMT
# Expires: Thu, 01 Oct 2020 08:23:36 GMT
# Server: BWS/1.1  # 网页的服务器
# Set-Cookie: BDSVRTM=228; path=/  # Cookie: 向浏览器发送追踪用户信息的变量设置。当用户浏览器不存在cookie时，将会把这个信息传递给浏览器。使得用户访问网页时按照变量设置返回信息
# Set-Cookie: BD_HOME=1; path=/
# Set-Cookie: H_PS_PSSID=32819_32617_1450_32791_31254_32230_7517_32116_26350; path=/; domain=.baidu.com
# Strict-Transport-Security: max-age=172800
# Traceid: 1601540616041153153013991771232840718763
# X-Ua-Compatible: IE=Edge,chrome=1
# Transfer-Encoding: chunked

# Header 与 Body 之间隔了一个空格。Header是连续的，只要有一个空行，那么空行之后的就是body

# 2. Body
# <!DOCTYPE html><!--STATUS OK-->
#
#     <html><head><meta http-equiv="Content-Type" content="text/html;charset=utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><meta content="always" name="referrer"><meta name="theme-color" content="#2932e1"><meta name="description" content="全球最大的中文搜索引擎、致力于让网民更便捷地获取信息，找到所求。百度超过千亿的中文网页数据库，可以瞬间找到相关的搜索结果。"><link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" /><link rel="search" type="application/opensearchdescription+xml" href="/content-search.xml" title="百度搜索" /><link rel="icon" sizes="any" mask href="//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg"><link rel="dns-prefetch" href="//dss0.bdstatic.com"/><link rel="dns-prefetch" href="//dss1.bdstatic.com"/><link rel="dns-prefetch" href="//ss1.bdstatic.com"/><link rel="dns-prefetch" href="//sp0.baidu.com"/><link rel="dns-prefetch" href="//sp1.baidu.com"/><link rel="dns-prefetch" href="//sp2.baidu.com"/><title>百度一下，你就知道</title>
# <style index="newi" type="text/css">#form