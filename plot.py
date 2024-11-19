import matplotlib.pyplot as plt
import numpy as np
def read_data_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        data = [list(map(float, line.split())) for line in lines]
    return data
def plot_data(series1, series2):
    x = list(range(1, len(series1) + 1))

    plt.plot(x, series1, label="Series 1", marker='', linestyle='-', color='blue')
    plt.plot(x, series2, label="Series 2", marker='', linestyle='--', color='orange')

    plt.title("Comparison")
    plt.xlabel("Количество элементов") #amount of elemnts
    plt.ylabel("Время (секунды)") #time(in seconds)

    y_min = min(min(series1), min(series2))
    y_max = max(max(series1), max(series2))
    y_ticks = np.linspace(y_min, y_max, num=6)
    plt.yticks(y_ticks, [f'{tick:.2e}' for tick in y_ticks])

    plt.grid(True)
    plt.legend()

    plt.show()


def main():
    filename = 'data.txt'
    data = read_data_from_file(filename)

    if len(data) < 4:
        print("Exception")
        return

    choice = input("1 - Stack, 2 - Queue:")

    if choice == "1":
        series1 = data[0]
        series2 = data[2]
    elif choice == "2":
        series1 = data[1]
        series2 = data[3]
    else:
        print("Incorrect choice")
        return

    # Построение графика
    plot_data(series1, series2)


# Запуск программы
if __name__ == "__main__":
    main()
