import random
import time
import matplotlib.pyplot as plt


# Детермінований QuickSort
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Обираємо середній елемент як опорний
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


# Рандомізований QuickSort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # Обираємо випадковий елемент як опорний
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


# Вимірювання часу виконання функцій сортування
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    return time.time() - start_time


# Генерація тестових масивів та вимірювання продуктивності
def compare_quick_sorts():
    sizes = [10_000, 50_000, 100_000, 500_000]
    results = {"deterministic": [], "randomized": []}

    for size in sizes:
        arr = [random.randint(1, 1_000_000) for _ in range(size)]

        # Вимірювання часу для детермінованого QuickSort
        det_times = [measure_time(deterministic_quick_sort, arr.copy()) for _ in range(5)]
        det_avg_time = sum(det_times) / len(det_times)
        results["deterministic"].append(det_avg_time)

        # Вимірювання часу для рандомізованого QuickSort
        rand_times = [measure_time(randomized_quick_sort, arr.copy()) for _ in range(5)]
        rand_avg_time = sum(rand_times) / len(rand_times)
        results["randomized"].append(rand_avg_time)

        print(f"\nРозмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {rand_avg_time:.4f} секунд")
        print(f"   Детермінований QuickSort: {det_avg_time:.4f} секунд")

    return sizes, results


# Побудова графіка результатів
def plot_results(sizes, results):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, results["randomized"], label="Рандомізований QuickSort", marker="o")
    plt.plot(sizes, results["deterministic"], label="Детермінований QuickSort", marker="o")
    plt.title("Порівняння рандомізованого та детермінованого QuickSort")
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.legend()
    plt.grid()
    plt.show()


# Основна функція для виконання порівняння
if __name__ == "__main__":
    sizes, results = compare_quick_sorts()
    plot_results(sizes, results)
