import json

python_value = {'name': 'Zophie', 'isCat': True, 'miceCaught': 0, 'felineIQ': None}

json_data = json.dumps(python_value)  # 利用 dumps(dump string) 可以将 Python 数据生成 json 数据
print(json_data)