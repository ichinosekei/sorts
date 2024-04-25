import subprocess
import numpy as np
import matplotlib.pyplot as plt
import time

# Функция для генерации массивов
for sad in range(2):
    def generate_array(size):
        if sad == 0:
            return np.random.randint(1, 100000, size=size).tolist()
        else:
            return np.random.randint(1, 2000000, size=size).tolist()

    # Функция для замера времени сортировки
    def measure_time(command, arr):
        total_time = 0
        # for _ in range(3):  # Проведение измерений 3 раза
        #     process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        #     input_data = ' '.join(map(str, arr)) + '\n'
        #     start_time = time.time()
        #     process.communicate(input=input_data)
        #     end_time = time.time()
        #     total_time += end_time - start_time
        # return total_time / 3  # Возвращаем среднее время

        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        input_data = ' '.join(map(str, arr)) + '\n'
        start_time = time.time()
        process.communicate(input=input_data)
        end_time = time.time()
        return end_time - start_time




    # Размеры массивов для тестирования
    if sad == 0:
        sizes = [100, 1000, 10000,50000, 100000, 500000 ,1000000]
    else:
        sizes = [100, 1000, 10000,50000, 100000]
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
    plt.figure(figsize=(10, 5))
    for name, t in times.items():
        if name == 'Bubble Sort':
            plot_sizes = sizes[:len(t)]  # Укорачиваем список размеров для пузырьковой сортировки
        else:
            plot_sizes = sizes  # Используем полный список размеров для остальных сортировок
        
        plt.plot(plot_sizes, t, label=name, marker='o')

    plt.title('Sorting Algorithm vs Array Size')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    # plt.xscale('log')
    plt.xscale('log')
    plt.yscale('log')  # Для лучшего отображения больших различий во времени


    plt.legend()
    plt.grid(True)
    plt.show()
