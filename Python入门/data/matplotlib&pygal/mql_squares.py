import matplotlib.pyplot as plt

squares_1 = [1, 2, 3, 4, 5]
squares_2 = [1, 4, 9, 16, 25]
plt.plot(squares_1, squares_2, 'r', label="line1", linewidth=5)
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Value", fontsize=14)
plt.tick_params("both", labelsize=14, color='r')
plt.show()
