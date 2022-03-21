import time
import subprocess

time_left = 10

while time_left > 0:
    print(time_left)
    time.sleep(1)
    time_left -= 1

    if 0 < time_left < - 5:
        subprocess.Popen(['xdg-open', '/home/ryan/Desktop/notify.wav'])
