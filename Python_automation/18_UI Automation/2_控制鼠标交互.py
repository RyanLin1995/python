import time
import pyautogui

# 鼠标移动到指定位置
# pyautogui.click(100, 120)  # click 是mouseDown 和 mouseUp 的封装以方便使用
# 按下鼠标
pyautogui.mouseDown(220, 220)
# 拖动鼠标到绝对位置
pyautogui.dragTo(600, 220)
pyautogui.dragRel(200, 100)  # dragRel 是拖动鼠标到相对位置
# 松开鼠标
pyautogui.mouseUp()
# 滚动鼠标
pyautogui.scroll(-100)  # 向下滚动
pyautogui.scroll(100)  # 向上滚动