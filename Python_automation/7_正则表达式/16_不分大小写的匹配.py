import re

# 在 re.compile 中添加 re.I 或 re.IGNORECASE 来进行忽略大小写的匹配

robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())
print(robocop.search('Al, why does your programming book talk about robocop so much?').group())

