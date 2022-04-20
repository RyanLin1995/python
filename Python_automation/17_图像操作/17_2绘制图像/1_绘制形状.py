from PIL import Image, ImageDraw

im = Image.new('RGBA', (200, 200), 'orange')  # 创建一个黑色背景的图片
draw = ImageDraw.Draw(im)  # 实例化一个画笔对象

# 绘制点
draw.point((7, 7), fill='pink')  # point()函数用来绘制点，参数为点的坐标和颜色，
# 坐标可以为元组或者元组[(x,y),(x,y)]/坐标[x1,y1,x2,y2]组成列表，
# 颜色可以为字符串，也可以为元组或者列表，默认为黑色

# 绘制线
draw.line((10, 10, 100, 100), fill='red')  # line()函数用来绘制线，参数参考 point()

# 绘制矩形
draw.rectangle((20, 20, 200, 200), fill='blue')  # rectangle()函数用来绘制矩形，
# 第一个参数为坐标，形式为(left, top, right, bottom)，
# left, top 值指定了矩形左上角的 x 和 y 坐标，right, bottom 指定了矩形右下角的 x 和 y 坐标，
# fill参数为颜色，outline参数为边框颜色。

# 绘制圆
draw.ellipse((120, 30, 160, 60), fill='green')  # ellipse()函数用来绘制圆，
# 参数参考 rectangle()，如果宽和高相等，则为圆形。

# 绘制多边形
draw.polygon([(57, 87), (79, 62), (94, 85), (120, 90), (103, 113)], fill='yellow')
# polygon()函数用来绘制多边形，参数参考 rectangle()。

im.show()
