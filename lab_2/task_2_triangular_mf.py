#task_2_triangular_mf.py
#Лаб 2. Завдання 2. Побудова трикутних функцій належності

import numpy as np
import matplotlib.pyplot as plt


def triangular_mf(x, a, b, c):
    """
    Математичний розрахунок трикутної функції належності μ(x).
    Параметри: a - ліва межа, b - вершина (значення 1), c - права межа.
    """
    return np.maximum(0, np.minimum((x - a) / (b - a + 1e-6), (c - x) / (c - b + 1e-6)))


def plot_cpu_temperature_mf(
        low_params=(20, 20, 55),
        normal_params=(35, 55, 75),
        high_params=(55, 90, 100),
        x_range=(20, 100),
        step=0.5,
        show_plot=True
):
    """
    Створює три нечіткі множини та будує їх на одному графіку.  Параметри:
      - low_params, normal_params, high_params: кортежі (a, b, c) для термів
      - x_range: діапазон температур (min, max)
      - step: крок дискретизації (°C)
      - show_plot: чи відображати графік одразу
    Повертає:
      - x: масив точок дискретизації
      - low, normal, high: масиви значень функцій належності
    """
    # Формуємо універсальну множину з кроком дискретизації
    x = np.arange(x_range[0], x_range[1] + step, step)

    # Обчислення функцій належності для кожного терму
    low = triangular_mf(x, *low_params)
    normal = triangular_mf(x, *normal_params)
    high = triangular_mf(x, *high_params)

    # 2. Побудова трьох функцій на одному графіку
    plt.figure(figsize=(9, 5))
    plt.plot(x, low, label=f'Низька {low_params}', color='blue', linewidth=2)
    plt.plot(x, normal, label=f'Нормальна {normal_params}', color='green', linewidth=2)
    plt.plot(x, high, label=f'Висока {high_params}', color='red', linewidth=2)

    # 3. Назви осей координат та заголовок
    plt.title('Трикутні функції належності для змінної «Температура процесора»')
    plt.xlabel('Температура процесора (°C)')
    plt.ylabel('Ступінь належності, μ(x)')

    # 4. Налаштування сітки, легенди та меж
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='upper right')
    plt.xlim(x_range[0], x_range[1])
    plt.ylim(0, 1.05)

    if show_plot:
        plt.show()

    return x, low, normal, high


# --- БЛОК ДЛЯ ТЕСТОВОГО ЗАПУСКУ ФАЙЛУ НАПРЯМУ ---
if __name__ == "__main__":
    plot_cpu_temperature_mf()