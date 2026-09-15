# task04_numpy_benchmark.py
# Лаб 1. Завдання 4. Дослідження швидкодії NumPy

import time
import numpy as np

# Кількість елементів для проведення тестування
ELEMENTS_COUNT = 10_000_000


def run_performance_test():
    formatted_count = f"{ELEMENTS_COUNT:,}".replace(",", " ")
    print(f"--- Порівняння швидкодії ({formatted_count} елементів) ---")

    # Підготовка даних для стандартних списків Python
    py_list_a = list(range(ELEMENTS_COUNT))
    py_list_b = list(range(1, ELEMENTS_COUNT + 1))

    # Підготовка даних для масивів NumPy
    np_arr_a = np.arange(ELEMENTS_COUNT)
    np_arr_b = np.arange(1, ELEMENTS_COUNT + 1)

    # 1. Додавання
    start_time = time.perf_counter()
    py_res = [a + b for a, b in zip(py_list_a, py_list_b)]
    py_add_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    np_res = np_arr_a + np_arr_b
    np_add_time = time.perf_counter() - start_time

    print(f"\n1. Додавання:")
    print(f"   Python: {py_add_time:.4f} сек")
    print(f"   NumPy:  {np_add_time:.4f} сек")
    print(f"   Прискорення: {py_add_time / np_add_time:.2f}x")

    # 2. Множення
    start_time = time.perf_counter()
    py_res = [a * b for a, b in zip(py_list_a, py_list_b)]
    py_mul_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    np_res = np_arr_a * np_arr_b
    np_mul_time = time.perf_counter() - start_time

    print(f"\n2. Множення:")
    print(f"   Python: {py_mul_time:.4f} сек")
    print(f"   NumPy:  {np_mul_time:.4f} сек")
    print(f"   Прискорення: {py_mul_time / np_mul_time:.2f}x")

    # 3. Пошук максимуму
    start_time = time.perf_counter()
    py_res = max(py_list_a)
    py_max_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    np_res = np.max(np_arr_a)
    np_max_time = time.perf_counter() - start_time

    print(f"\n3. Максимум:")
    print(f"   Python: {py_max_time:.4f} сек")
    print(f"   NumPy:  {np_max_time:.4f} сек")
    print(f"   Прискорення: {py_max_time / np_max_time:.2f}x")

    # 4. Обчислення середнього значення
    start_time = time.perf_counter()
    py_res = sum(py_list_a) / len(py_list_a)
    py_mean_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    np_res = np.mean(np_arr_a)
    np_mean_time = time.perf_counter() - start_time

    print(f"\n4. Середнє значення:")
    print(f"   Python: {py_mean_time:.4f} сек")
    print(f"   NumPy:  {np_mean_time:.4f} сек")
    print(f"   Прискорення: {py_mean_time / np_mean_time:.2f}x")
    print("-----------------------------------------------")


if __name__ == '__main__':
    run_performance_test()