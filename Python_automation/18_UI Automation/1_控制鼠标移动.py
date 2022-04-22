import pyautogui

# 设置每次操作的延时
pyautogui.PAUSE = 1

# 启用防故障模式
pyautogui.FAILSAFE = True

for i in range(10):
    # moveTo() 方法可以控制鼠标移动到指定的坐标位置，duration可以指定移动的时间。
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)

for i in range(10):
    # moveRel() 方法可以控制鼠标移动到相对的坐标位置
    pyautogui.moveRel(100, 0, duration=0.25)
    print(pyautogui.position())  # 返回鼠标当前的坐标位置
    pyautogui.moveRel(0, 100, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0, -100, duration=0.25)