#Лабораторна робота №1

import task01_check_imports
import task02_libs_structure
import task03_libs_depends
import task04_numpy_benchmark
import task06_pyswarms_review

if __name__ == '__main__':
    # Завдання 1. Створення робочого програмного середовища
    task01_check_imports.show_lib_versions()

    # Завдання 2. Аналіз структури бібліотек Python
    task02_libs_structure.inspect_libraries()

    # Завдання 3. Аналіз залежностей бібліотек
    task03_libs_depends.print_dep_tree()

    #Завдання 4. Дослідження швидкодії NumPy
    task04_numpy_benchmark.run_performance_test()

    #Завдання 6. Аналіз офіційної документації. Офіційний приклад з документації PySwarms: Training a Neural Network
    task06_pyswarms_review.run_performance_test()



