# 1. or 的短路求值特性。
# 短路求值：如果左边表达式为真，则右边表达式不会被求值。
# 但是注意：or 的短路特性，是对变量布尔值真假的计算。所以 None, 0, False, [], {} 等等，都是假。

def update_dict(context_dict: dict):
    context_dict.setdefault("name", "default_name")


blank_context = {}
str_context = {"a": "a"}
# if context:
#     update_dict(context)
#
# 可以利用 or 的短路特性，简化代码
update_dict(blank_context or {})
print(blank_context)

update_dict(str_context or {})
print(str_context)
