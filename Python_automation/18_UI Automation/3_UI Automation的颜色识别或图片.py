import pyautogui

# screenshot() 方法返回屏幕截图对象
im = pyautogui.screenshot()
# getPixel() 方法返回屏幕像素点的颜色
print(im.getpixel((150, 400)))
# pixelMatchesColor() 方法判断像素点的颜色是否与给定的颜色相同，极其不稳定，不建议使用
try:
    a = pyautogui.pixelMatchesColor(150, 400, (255, 255, 255))
except OSError:
    a = False
print(a)
# 代替方法：
print(im.getpixel((150, 400)) == (255, 255, 255))

# 图像识别
# locateOnScreen() 方法返回图像的位置，如果没有找到，返回None
icon = pyautogui.locateOnScreen('images/icon.png')
pyautogui.center(icon)  # 点击获取到的图像中心点
pyautogui.click(icon, button='right')  # 右键点击
