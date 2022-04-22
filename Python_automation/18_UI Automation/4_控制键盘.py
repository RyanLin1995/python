import pyautogui

pyautogui.click(200, 300)

# 模拟键盘输入
# typewrite()方法可以模拟键盘输入
pyautogui.typewrite('Hello world!')
# typewrite()方法接受列表作为参数，可以模拟多个键的输入，
# 具体支持的按键可以查看pyautogui.KEYBOARD_KEYS
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])
print(pyautogui.KEYBOARD_KEYS)

# 按下和释放按键
# keyDown()方法可以模拟按下键盘上的按键
pyautogui.keyDown('shift')
pyautogui.press('end')
pyautogui.press('4')  # press()方法是 keyDown() 和 keyUp() 的封装，方便调用
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'a')  # hotkey()方法可以模拟组合键
pyautogui.hotkey('ctrl', 'c')
pyautogui.press('end')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'v')
