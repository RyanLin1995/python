import matplotlib.pyplot as plt

# x_values = [1, 3, 5, 7, 9]
# y_values = [2, 4, 6, 8, 10]
#
# plt.scatter(x_values, y_values, s=200)
# # plt.scatter(2,4, s=200)
# # 设置图表标题并给坐标加上标签
# plt.gl_title("Square Number", fontsize=24)
# plt.xlabel("value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# # 设置刻度标记的大小
# plt.tick_params(axis="both", labelsize=10)
# plt.show()
from numpy.ma import arange

x_values = list(range(1, 10))
y_values = [x ** 2 for x in x_values]

plt.scatter(x_values, y_values, s=50, edgecolor="none", c=y_values, cmap="Blues")
plt.title("Square Number", fontsize=10)
plt.xlabel("Value", fontsize=10)
plt.ylabel("Square Value", fontsize=10)
plt.tick_params(axis="both", labelsize=8)
# plt.axis([0,10, 0,100])
plt.xticks([1, 2, 3, 4, 5, 6])
plt.yticks([600, 500, 400, 300, 200, 100])
plt.savefig("test.png", format="png")
plt.show()
