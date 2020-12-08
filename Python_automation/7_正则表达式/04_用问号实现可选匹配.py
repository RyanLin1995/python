import re

# 想匹配的内容是可选的，可以使用字符?
# 意思是匹配这个问号前的分组零次或一次
# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search("The adventures of Batman")
# print(mo1.group())
# mo2 = batRegex.search("The adventures of Batwoman")
# print(mo2.group())

# phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo1 = phoneNumRegex.search("The phone number is 433-221-0033")
phoneNumRegex = re.compile(r'(\(\d\d\d\) )?\d\d\d-\d\d\d\d')
mo1 = phoneNumRegex.search("The phone number is (433) 221-0033")
print(mo1.group())
mo2 = phoneNumRegex.search("The phone number is 221-0033")
print(mo2.group())
