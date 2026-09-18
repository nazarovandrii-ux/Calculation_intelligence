#task_1_universal_set.py
#Лаб 2. Завдання 1. Побудова універсальної множини

import numpy as np
import matplotlib.pyplot as plt


def get_universal_set(start=20, stop=100, step=0.5, show_plot=True):
    """
    Створює універсальну множину температур процесора та будує її графік.

    Параметри:
      - start: мінімальна температура (°C)
      - stop: максимальна температура (°C)
      - step: крок дискретизації (°C)
      - show_plot: чи відображати графік одразу

    Повертає:
      - X: одномірний масив NumPy з точками дискретизації
    """
    # Генеруємо масив точок
    X = np.arange(start, stop + step, step)

    # Побудова графіка
    plt.figure(figsize=(9, 2.5))
    plt.plot(X, np.zeros_like(X), 'b|', markersize=10, label='Точки дискретизації')
    plt.title('Візуалізація точок універсальної множини')
    plt.xlabel('Температура процесора (°C)')
    plt.yticks([])  # Прибираємо вісь Y
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlim(start - 2, stop + 2)
    plt.legend()
    plt.tight_layout()

    if show_plot:
        plt.show()

    return X


# --- БЛОК ДЛЯ ТЕСТОВОГО ЗАПУСКУ ФАЙЛУ НАПРЯМУ ---
if __name__ == "__main__":
    # Виклик функції з параметрами за замовчуванням
    X = get_universal_set()
    print(f"Створено множину: від {X[0]}°C до {X[-1]}°C (усього точок: {len(X)})")