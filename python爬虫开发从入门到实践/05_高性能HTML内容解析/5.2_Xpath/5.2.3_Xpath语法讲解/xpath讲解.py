import lxml.html

# 1. Xpath 语句样式
# 获取文本：//标签1[@属性1="属性值1"]/标签2[@属性2="属性值2"]/.../text()
# 获取属性值：//标签1[@属性1="属性值1"]/标签2[@属性2="属性值2"]/.../@属性n
source = '''
<html>
  <head>
    <title>测试</title>
  </head>
  <body>
    <div class="useful">
      <ul>
        <li class="info">我需要的信息1</li>
        <li class="info">我需要的信息2</li>
        <li class="info">我需要的信息3</li>
      </ul>
     </div>
     <div class="useless">
       <ul>
         <li class="info">垃圾1</li>
         <li class="info">垃圾2</li>
       </ul>
     </div>
  </body>
</html>
'''
selector = lxml.html.fromstring(source)
info = selector.xpath('//div[@class="useful"]/ul/li/text()')
print(info)

###############################################################

# 2. XPath 的特殊情况
# （1）以相同字符串开头：//标签[start-with(@属性名,"相同的开头部分")]
html1 = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div id="test-1-k">需要的内容1</div>
    <div id="test-2-k">需要的内容2</div>
    <div id="testfault-k">需要的内容3</div>
    <div id="useless">这是我不需要的内容</div>
</body>
</html>
'''
selector1 = lxml.html.fromstring(html1)
info1 = selector1.xpath('//div[starts-with(@id,"test")]/text()')
print(info1)

# (2) 属性值包含相同字符串：//标签[contains(@属性名,"相同的部分")]
html2 = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div id="abc-key-x">需要的内容1</div>
    <div id="123-key-000">需要的内容2</div>
    <div id="haha-key">需要的内容3</div>
    <div id="useless">这是我不需要的内容</div>
</body>
</html>
'''
selector2 = lxml.html.fromstring(html2)
info2 = selector2.xpath('//div[contains(@id,"-key")]/text()')
print(info2)

# (3) 对 XPath 返回的对象执行 XPath：先抓大再抓小
html3 = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div id="test3">
        我左青龙，
        <span id="tiger">
            右白虎，
            <ul>上朱雀，
                <li>下玄武。</li>
            </ul>
            老牛在当中，
        </span>
        龙头在胸口。
    </div>
</body>
</html>
'''
selector3 = lxml.html.fromstring(html3)
# 先通过抓取大的范围
data = selector3.xpath('//div[@id="test3"]')  # 这里返回一个列表
info3 = data[0].xpath('string(.)')  # 使用string(.)就可以把数据获取完整
print(info3)
