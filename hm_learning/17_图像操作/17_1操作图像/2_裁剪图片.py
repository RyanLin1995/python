from PIL import Image

# corp 方法可用于裁剪图片，接收一个元组作为参数，元组的元素分别为：左边界，上边界，右边界，下边界）
cat_img = Image.open('zophie.png')
crop_img = cat_img.crop((335, 345, 565, 560))
crop_img.save('crop_zophie.png')
