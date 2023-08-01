from operator import itemgetter

metro_data = [
    ('Tokyo', 'JP', 36.93, (35.68, 139.69)),
    ('Delhi NCR', 'IN', 21.94, (28.61, 77.21)),
    ('Mexico City', 'MX', 20.14, (19.43, -99.13)),
    ('New York-Newark', 'US', 20.1, (40.81, -74.02)),
    ('Sao Paulo', 'BR', 19.65, (-23.55, -46.64))
]

for city in sorted(metro_data, key=itemgetter(1)):  # 这里展示了 itemgetter 可以根据元组的某个字段对元祖列表进行排序
    print(city)

cc_name = itemgetter(1, 0)  # 这里展示了传递多个索引参数给 itemgetter 后，itemgetter 所构建的函数就会返回提取的值构成的元组
for city in metro_data:
    print(cc_name(city))
