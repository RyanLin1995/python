import time

import uiautomator2 as u2

d = u2.connect('127.0.0.1:16384')
d(text="KN Lymiac9.11").click()
d.xpath('//*[@resource-id="com.tencent.mm:id/o4q"]').click()
for i in range(11):
    d.send_keys(f"你是猪{i}")
    time.sleep(0.5)
    d(text='发送').click()
