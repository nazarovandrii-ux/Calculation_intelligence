# task_3_gaussian_mf.py
# Лаб 2. Завдання 3. Порівняння різних типів функцій належності

import numpy as np
import matplotlib.pyplot as plt

# Імпортуємо формування універсальної множини з Завдання 1
from task_1_universal_set import get_universal_set


def gaussian_mf(x, mean, sigma):
    """
    Математичний розрахунок Гаусової функції належності μ(x).
    Параметри: mean - центр (вершина, де μ=1), sigma - ширина.
    """
    return np.exp(-((x - mean) ** 2) / (2 * (sigma ** 2)))


def plot_gaussian_mf(
        gauss_params={'low': (20, 10), 'normal': (55, 10), 'high': (90, 10)},
        show_plot=True
):
    """
    Будує один графік із трьома Гаусовими функціями належності.
    """
    # Отримуємо універсальну множину з Завдання 1 без показу її графіка
    x = get_universal_set(show_plot=False)

    # 1. Обчислення Гаусових функцій
    g_low = gaussian_mf(x, *gauss_params['low'])
    g_normal = gaussian_mf(x, *gauss_params['normal'])
    g_high = gaussian_mf(x, *gauss_params['high'])

    # 2. Побудова ОДНОГО графіка
    plt.figure(figsize=(9, 4.5))
    plt.plot(x, g_low, label=f"Низька (mean={gauss_params['low'][0]}, sigma={gauss_params['low'][1]})", color='blue', linewidth=2)
    plt.plot(x, g_normal, label=f"Нормальна (mean={gauss_params['normal'][0]}, sigma={gauss_params['normal'][1]})", color='green', linewidth=2)
    plt.plot(x, g_high, label=f"Висока (mean={gauss_params['high'][0]}, sigma={gauss_params['high'][1]})", color='red', linewidth=2)

    # 3. Налаштування осей, заголовка та легенди
    plt.title('Гаусові функції належності для «Температури процесора»')
    plt.xlabel('Температура процесора (°C)')
    plt.ylabel('Ступінь належності, μ(x)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='upper right')
    plt.xlim(20, 100)
    plt.ylim(0, 1.05)
    plt.tight_layout()

    if show_plot:
        plt.show()

    return x, g_low, g_normal, g_high


# --- БЛОК ДЛЯ САМОСТІЙНОГО ЗАПУСКУ ---
if __name__ == "__main__":
    plot_gaussian_mf()