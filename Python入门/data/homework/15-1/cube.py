import matplotlib.pyplot as plt

# x_values = [1, 3, 5, 7, 9]
x_values = list(range(0, 5000))
y_values = [x ** 3 for x in x_values]

# plt.plot(x_values, y_values, color="Red", lw=10)
plt.scatter(x_values, y_values, s=10, c=x_values, cmap="Accent")
plt.title("Cube", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube Value", fontsize=14)
plt.tick_params(axis="both", labelsize=10)
plt.axis([0, 5000, 0, 100000000000])
plt.show()
