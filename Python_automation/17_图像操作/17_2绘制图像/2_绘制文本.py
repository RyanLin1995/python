from PIL import Image, ImageDraw, ImageFont

im = Image.new('RGB', (200, 200), (255, 255, 255))
draw = ImageDraw.Draw(im)
draw.text((0, 0), 'Hello', fill='purple')  # 第一个参数是坐标，第二个参数是文本，第三个参数是颜色
arial_font = ImageFont.truetype('arial.ttf', 40)  # 第一个参数是字体文件，第二个参数是字体大小
draw.text((0, 50), 'Hello', fill='red', font=arial_font)  # 第一个参数是坐标，第二个参数是文本，第三个参数是颜色，第四个参数是字体
im.show()