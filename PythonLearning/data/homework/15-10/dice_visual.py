import matplotlib.pyplot as plt
from die import Die

# 创建两个D8
die_1 = Die(8)
die_2 = Die(8)
results = list(map(lambda x: die_1.roll() + die_2.roll(), range(1000)))

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# 对结果进行可视化
# hist = pygal.Bar()
#
# hist.title = "Results of rolling two D8 1000 times"
# hist.x_labels = map(str, range(2, max_result + 1))
# hist.x_title = "Result"
# hist.y_title = "Frequency of result"
# hist.add("D8 * D8", frequencies)
# hist.render_to_file("test_two_D8.svg")
# hist.render_in_browser()

# plt.plot(range(2, max_result + 1), frequencies, "r", )
# plt.title("Results of rolling two D8 1000 times")
# plt.xlabel("Result")
# plt.ylabel("Frequency of result")
# plt.tick_params("both", labelsize=14, color='r')
# plt.xticks(range(2, max_result+1))
# plt.show()

plt.scatter(range(2, max_result + 1), frequencies, c=frequencies, cmap="Reds", edgecolors=None, s=10)
plt.title("Results of rolling two D8 1000 times")
plt.xlabel("Result")
plt.ylabel("Frequency of result")
plt.tick_params("both", labelsize=14, color='r')
plt.xticks(range(2, max_result+1))
plt.show()
plt.show()

