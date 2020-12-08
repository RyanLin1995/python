from random_walk import RandomWalk
import matplotlib.pyplot as plt
import sys

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_number = list(range(rw.num_points))
    plt.figure(figsize=(8, 4), dpi=128)
    plt.scatter(rw.x_values, rw.y_values, c=point_number, cmap="Blues", edgecolors=None, s=1)
    plt.scatter(0, 0, c="Green", edgecolors=None, s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="Red", edgecolors=None, s=100)
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    plt.xticks([])  # 隐藏坐标轴
    plt.yticks([])  # 隐藏坐标轴
    plt.show()

    keep_running = input("Make anthoer walk? (y/n): ")
    if keep_running == "n" or keep_running == "N":
        break
    if keep_running == "q":
        sys.exit()
