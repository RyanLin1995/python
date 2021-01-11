import pygal
from die import Die

# 创建一个D6
die = Die()


# 掷几次骰子,并将结果存储在一个列表中
# results = []
# for roll_num in range(100):
#     result = die.roll()
#     results.append(result)

# def check_result(num_list):
#     for x in num_list:
#         if x in list(range(1, 7)):
#             return "Yes"
#         else:
#             return "No"

results = list(map(lambda x: die.roll(), range(1000)))
# print(results)
# print(check_result(results))

# 分析结果
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = map(str, range(1, die.num_sides + 1))
hist.x_title = "Result"
hist.y_title = "Frequency of result"
hist.add("D6", frequencies)
hist.render_to_file("test.svg")
hist.render_in_browser()
