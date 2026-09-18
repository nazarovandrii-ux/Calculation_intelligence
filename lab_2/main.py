#Лабораторна робота №2

import task_1_universal_set
from lab_2 import task_2_triangular_mf
from lab_2.task_3_gaussian_mf import plot_gaussian_mf
from lab_2.task_4_custom_variable import plot_ram_usage_mf

if __name__ == '__main__':
    # Завдання 1. Побудова універсальної множини
    task_1_universal_set.get_universal_set()

    # Завдання 2. Побудова трикутних функцій належності
    task_2_triangular_mf.plot_cpu_temperature_mf()

   # Завдання 3. Порівняння різних типів функцій належності
    x, g_low, g_normal, g_high = plot_gaussian_mf()

    #Завдання 4. Побудова власної нечіткої змінної (RAM)
    x, ram_low, ram_medium, ram_high = plot_ram_usage_mf()


