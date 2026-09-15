#task02_libs_structure.py
#Лаб 1. Завдання 2. Аналіз структури бібліотек Python

import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as fuzzyControl
import pyswarms as ps
import inspect
from deap import base


def inspect_libraries():
    # Довідка про модулі та класи
    help(np.ndarray)
    help(fuzzyControl)
    help(base.Toolbox)
    help(ps.single.GlobalBestPSO)

    # Перелік доступних атрибутів і методів
    print(dir(np))
    print(dir(fuzzy))
    print(dir(base))
    print(dir(ps.single))

    # Перегляд сигнатур функцій і методів
    print(inspect.signature(np.mean))
    print(inspect.signature(fuzzy.trimf))
    print(inspect.signature(base.Toolbox.register))
    print(inspect.signature(ps.single.GlobalBestPSO))

    # Перегляд документації об’єкта
    print(inspect.getdoc(np.linalg.solve))
    print(inspect.getdoc(ps.single.GlobalBestPSO))

if __name__ == '__main__':
    inspect_libraries()



