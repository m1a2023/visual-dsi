import matplotlib.pyplot as plt

# Example data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
series1 = [19, 111, 11, 10, 11, 11, 1, 10, 18, 5, 11]  # First series (like "Series 1")
series2 = [12, 0, 90, 11, 1, 0, 9, 19, 19, 18, 1]      # Second series (like "Series 2")

# Create a line plot
plt.plot(x, series1, label="Series 1", marker='o', linestyle='-', color='blue')
plt.plot(x, series2, label="Series 2", marker='s', linestyle='--', color='orange')

# Add chart elements
plt.title("Comparision")
plt.xlabel("Items")
plt.ylabel("Values")
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
