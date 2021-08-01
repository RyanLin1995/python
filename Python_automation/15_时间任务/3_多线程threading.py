import threading
import time

# 1. threading demo
print("Start a program")


def take_a_nap():
    time.sleep(5)
    print("Wake Up!")


T1 = threading.Thread(target=take_a_nap)
T1.start()

print("End a program")

# 2. threading 传参
# 常规参数用列表传递，关键字参数用字典传递
T2 = threading.Thread(target=print, args=["Cat", "Dog", "Forgs"], kwargs={"sep": " & "})
T2.start()