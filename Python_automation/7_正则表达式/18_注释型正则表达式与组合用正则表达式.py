import re

# 当你的正则表达式过于复杂时，可以使用 re.VERBOSE 给正则表达式添加注释
re.compile(r"(\d{3}|\(\d{3}\))?  # area code "
           r"(\s|-|.)?  # separator"
           r"\d{3}  # first3 digits"
           r"(\s|-|.)?  # separator"
           r"\d{4} # last 4 digits"
           r"(\s*(ext|x|ext.)\s*\d{2,5})? # extension"
           r")", re.VERBOSE)

# 但如果你想正则表达式既忽略大小写，又匹配 . 换行，可以用 |
re.compile('foo', re.I | re.DOTALL)