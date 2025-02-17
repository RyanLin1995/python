def extract_value(data: str):
    """
    当 data 包含分隔符 : 时，元组最后一个成员刚好是 value。
    如果没有分隔符，最后一个成员默认为空字符串 ''
    :param data:
    :return:
    """
    return data.partition(":")[-1]  # partition() 返回元组，结果是 (head, sep, tail)


print(extract_value("abc:123"))
print(extract_value("abc"))
print("-" * 50)

s = "明明是中文,却使用了英文标点."
# 创建替换规则表：',' -> '，' ; '.' -> '。'
table = s.maketrans(
    ",.", "，。"
)  # maketrans 方法，返回一个替换表，用于给 translate 方法替换字符串中的字符
print(s.translate(table))
