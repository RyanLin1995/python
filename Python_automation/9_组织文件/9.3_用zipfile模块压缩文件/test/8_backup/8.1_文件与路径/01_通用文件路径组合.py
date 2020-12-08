import os

# 通过 os.path.join() 方法，可以自适应生成对应路径
# 如: 生成一个 usr/bin/spam
ret = os.path.join('usr', 'bin', 'spam')
print(ret)

# 但是该程序在 Windows 下生成的路径为 usr\\bin\\spam

# 案例:
myFiles = ['account.txt', 'details.csv', 'invite.docx']
for file in myFiles:
    print(os.path.join("test", file))
