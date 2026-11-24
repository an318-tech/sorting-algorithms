import random
import time
import matplotlib.pyplot as plt


# сортировка пузырьком
def bubble_sort(arr):
    result = list(arr)
    n = len(result)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result

# сортировка выбором
def selection_sort(arr):
    result = list(arr)
    n = len(result)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        if min_idx != i:
            result[i], result[min_idx] = result[min_idx], result[i]
    return result

# сортировка вставками
def insertion_sort(arr):
    result = list(arr)
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result

# среднее время работы функции на списке arr
def measure_time(sort_func, arr, repeats=3):
    total = 0.0
    for _ in range(repeats):
        start = time.perf_counter()
        sort_func(arr)
        total += time.perf_counter() - start
    return total / repeats

# сравнение алгоритмов на случайных списках и постройка графика
def run_benchmark(sizes=(100, 200, 400, 800, 1600, 3200), seed=42):
    random.seed(seed)
    algorithms = {
        'Пузырьком': bubble_sort,
        'Выбором': selection_sort,
        'Вставками': insertion_sort,
    }
    timings = {name: [] for name in algorithms}

    print(f"{'Размер':>8} | " + " | ".join(f"{name:>10}" for name in algorithms))
    print('-' * 50)
    for size in sizes:
        data = [random.randint(-10_000, 10_000) for _ in range(size)]
        row = []
        for name, func in algorithms.items():
            t = measure_time(func, data)
            timings[name].append(t)
            row.append(f'{t:.4} c')
        print(f'{size:>8} | ' + ' | '.join(f'{cell:>10}' for cell in row))

    plt.figure(figsize=(9, 5.5))
    for name, times in timings.items():
        plt.plot(sizes, times, marker='o', label=name)
    plt.xlabel('Размер списка, элементов')
    plt.ylabel('Среднее время, с')
    plt.title('Сравнение времени сортировки: пузырек, выбор, вставки')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('benchmark.png', dpi=150)
    print('График сохранен в benchmark.png')


if __name__ == '__main__':
    sample = [5, 1, 4, 2, 8, 0, -3]
    assert bubble_sort(sample) == sorted(sample)
    assert selection_sort(sample) == sorted(sample)
    assert insertion_sort(sample) == sorted(sample)
    print('Проверка корректности пройдена\n')

    run_benchmark()