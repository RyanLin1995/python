import win32gui

hwnd = win32gui.FindWindow(None, f"PID:123")
print(win32gui.IsWindowVisible(hwnd))
