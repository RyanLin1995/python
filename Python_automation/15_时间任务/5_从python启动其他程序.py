import os
import time
import subprocess

# 1. 打开一个新的计算器
# cal = subprocess.Popen(r'/usr/bin/deepin-calculator')
# print(cal)  # 返回的是一个Popen对象
# print(cal.poll())  # poll 方法用于检查进程是否结束，如果正常结束返回0，否则返回 None 或 -N（如果是非0的错误码）
# time.sleep(3)
# os.kill(cal.pid, 9)  # 9代表SIGKILL，即kill -9
# time.sleep(3)
# print(cal.wait())  # wait 方法用于等待进程结束，其将会堵塞代码。如果正常结束返回0，否则返回错误码
# print(cal.poll())

# 2. 给打开的计算器输入一个数字
# log_file = subprocess.Popen([r'/usr/bin/gedit', '/home/ryan/cv_debug.log'])  # 给 Popen 对象传入一个列表，
# # 列表中的第一个元素是要执行的程序，后面的元素是程序的参数，传入的程序在执行时是一个独立的进程
# print(log_file)

# 3. 使用默认程序打开文件
default = subprocess.Popen(['xdg-open', '/home/ryan/Desktop/wallhaven-96w8e8.png'])  # 每个操作系统都有一个默认的程序，
# Windows下默认是 'start' 程序，Mac 是 'open', Ubuntu 是 'xdg-open' 或 'see'
print(default)