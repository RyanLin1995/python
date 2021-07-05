import json

data = '{"name":"Zophie", "isCat":true, "miceCaught":0, "felineIQ": null}'

json_data = json.loads(data)  # 利用 loads(load string) 方法可以读取 json 数据，返回的是一个字典
print(json_data)