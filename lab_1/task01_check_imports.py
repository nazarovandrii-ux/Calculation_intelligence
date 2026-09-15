#task01_check_imports.py
#Лаб 1. Завдання 1. Створення робочого програмного середовища

import numpy as np
import matplotlib
import skfuzzy as fuzzy
import deap
import pyswarms as ps


def show_lib_versions():
    print("--- Перевірка імпорту ---")
    print(f"NumPy версія: {np.__version__}")
    print(f"Matplotlib версія: {matplotlib.__version__}")
    print(f"Scikit-fuzzy версія: {fuzzy.__version__}")
    print(f"DEAP версія: {deap.__version__}")
    print(f"PySwarms версія: {ps.__version__}")
    print("------------------------")

if __name__ == '__main__':
    show_lib_versions()



