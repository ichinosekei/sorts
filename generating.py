import subprocess
import numpy as np
import matplotlib.pyplot as plt
import time

# Функция для генерации массивов
for sad in range(3):
    def generate_array(size):
        if sad == 1:
            return np.random.randint(1, 100000, size=size).tolist()
        elif sad == 2:
            return np.random.randint(1, 2000000, size=size).tolist()
        else:
            return np.random.randint(1, 1000, size=size).tolist()
    # Функция для замера времени сортировки
    def measure_time(command, arr):
        total_time = 0
        for _ in range(3):  # Проведение измерений 3 раза
            process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            input_data = ' '.join(map(str, arr)) + '\n'
            start_time = time.time()
            process.communicate(input=input_data)
            end_time = time.time()
            total_time += end_time - start_time
        return total_time / 3  # Возвращаем среднее время

        # process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # input_data = ' '.join(map(str, arr)) + '\n'
        # start_time = time.time()
        # process.communicate(input=input_data)
        # end_time = time.time()
        # return end_time - start_time




    # Размеры массивов для тестирования
    
    # sizes = [100, 1000, 5000, 10000, 20000, 40000, 80000, 100000, 250000]
    sizes =  [100, 1000, 2500, 7500, 10000]

    sorting_algorithms = {
        'Merge Sort': ['./sort_app', 'merge'],
        'Quick Sort': ['./sort_app', 'quick'],
        'Bubble Sort': ['./sort_app', 'bubble'],
        'Radix Sort': ['./sort_app', 'radix'],
        'Counting Sort': ['./sort_app', 'counting'],
        'Heap Sort': ['./sort_app', 'heap']
    }
    # Словарь для хранения времен выполнения
    times = {name: [] for name in sorting_algorithms}

    # Замер времени
    for size in sizes:
        arr = generate_array(size)
        for name, path in sorting_algorithms.items():
            if size >= 100000 and name == 'Bubble Sort':
                continue  # Пропускаем Bubble Sort для больших размеров
            t = measure_time(path, arr)
            times[name].append(t)

    # Построение графика
    plt.figure(figsize=(12, 6))
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
    k = 0
    for name, t in times.items():
        if name == 'Bubble Sort':
            plot_sizes = sizes[:len(t)]  # Укорачиваем список размеров для пузырьковой сортировки
        else:
            plot_sizes = sizes  # Используем полный список размеров для остальных сортировок

        coefic = np.polyfit(plot_sizes, t, 2)
        polynomial = np.poly1d(coefic)
        plt.plot(plot_sizes, t, label=name, marker='o', color= colors[k])
        # plt.plot(np.array(sizes), poly(np.array(sizes)), label=f'{name} Fit')
        x_values = np.linspace(min(plot_sizes) * 10, max(plot_sizes) * 2, 400)
        y_values = polynomial(x_values)
        plt.plot(x_values, y_values, color=colors[k],label=name + ' апроксимация', alpha=0.75, linestyle='dashed')
        k += 1
        print(polynomial)
    plt.title('Sorting Algorithm vs Array Size')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    # plt.xscale('log')
    plt.xscale('log')
    plt.yscale('log')  # Для лучшего отображения больших различий во времени


    plt.legend()
    plt.grid(True)
    plt.show()