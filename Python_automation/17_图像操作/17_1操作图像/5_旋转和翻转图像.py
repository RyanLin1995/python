from PIL import Image

cat_img = Image.open('zophie.png')

# rotate() 方法可以旋转图像，传入的参数为角度
cat_img.rotate(90).save('zophie_rotate90.png')
cat_img.rotate(180).save('zophie_rotate180.png')
cat_img.rotate(270).save('zophie_rotate270.png')

# expaned 参数可以放大图像尺寸以适应画面
cat_img.rotate(6).save('zophie_rotate6.png')
cat_img.rotate(6, expand=True).save('zophie_rotate6_expanded.png')

# transpose() 方法可以翻转图像，传入的参数为 0, 1, 2, 3 分别代表水平翻转，垂直翻转，左右翻转，
# 水平垂直翻转

# 水平翻转
cat_img.transpose(0).save('zophie_flip_0.png')
# 水平翻转也可以传入 Image.FLIP_LEFT_RIGHT 参数
# cat_img.transpose(Image.FLIP_LEFT_RIGHT).save('zophie_horizontal.png')

# 垂直翻转
cat_img.transpose(1).save('zophie_flip_1.png')
# 垂直翻转也可以传入 Image.FLIP_TOP_BOTTOM 参数
# cat_img.transpose(Image.Image.FLIP_TOP_BOTTOM).save('zophie_vertical.png')

# 左右翻转
cat_img.transpose(2).save('zophie_flip_2.png')

# 水平垂直翻转
cat_img.transpose(3).save('zophie_flip_3.png')