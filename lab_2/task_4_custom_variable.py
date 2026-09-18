# task_4_custom_variable.py
# Лаб 2 Завдання 4. Побудова власної нечіткої змінної (RAM)

import numpy as np
import matplotlib.pyplot as plt


def trapezoidal_mf(x, a, b, c, d):
    """Трапецієподібна функція належності."""
    return np.maximum(0, np.minimum(np.minimum((x - a) / (b - a + 1e-6), 1), (d - x) / (d - c + 1e-6)))


def triangular_mf(x, a, b, c):
    """Трикутна функція належності."""
    return np.maximum(0, np.minimum((x - a) / (b - a + 1e-6), (c - x) / (c - b + 1e-6)))


def plot_ram_usage_mf(show_plot=True):
    """
    Побудова функцій належності для лінгвістичної змінної 'Завантаження RAM'.
    """
    # 1. Універсальна множина: 0 - 100 % з кроком 0.5 %
    x = np.arange(0, 100.5, 0.5)

    # 2–3. Формування термів та обчислення функцій
    # Низька: Трапеція (0, 0, 20, 45)
    ram_low = trapezoidal_mf(x, 0, 0, 20, 45)

    # Помірна: Трикутник (30, 50, 75)
    ram_medium = triangular_mf(x, 30, 50, 75)

    # Висока: Трапеція (60, 85, 100, 100)
    ram_high = trapezoidal_mf(x, 60, 85, 100, 100)

    # 4. Побудова графіків
    plt.figure(figsize=(9, 4.5))
    plt.plot(x, ram_low, label='Низька (0-45 %)', color='green', linewidth=2)
    plt.plot(x, ram_medium, label='Помірна (30-75 %)', color='orange', linewidth=2)
    plt.plot(x, ram_high, label='Висока (60-100 %)', color='red', linewidth=2)

    plt.title('Функції належності для змінної «Використання оперативної пам\'яті»')
    plt.xlabel('Завантаження RAM (%)')
    plt.ylabel('Ступінь належності, μ(x)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='upper right')
    plt.xlim(0, 100)
    plt.ylim(0, 1.05)
    plt.tight_layout()

    if show_plot:
        plt.show()

    return x, ram_low, ram_medium, ram_high


if __name__ == "__main__":
    plot_ram_usage_mf()