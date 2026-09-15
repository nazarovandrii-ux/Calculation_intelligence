# task03_libs_depends.py
# Лаб 1. Завдання 3. Аналіз залежностей бібліотек

import subprocess
import sys

def print_dep_tree():
    packages = "scikit-fuzzy,deap,pyswarms,scipy,matplotlib"
    cmd = [sys.executable, "-m", "pipdeptree", "-p", packages]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("=== ДЕРЕВО ЗАЛЕЖНОСТЕЙ (через pipdeptree) ===\n")
        print(result.stdout)
    except FileNotFoundError:
        print("Помилка: pipdeptree не встановлено. Виконайте: pip install pipdeptree")
    except subprocess.CalledProcessError as e:
        print(f"Помилка виконання команди: {e.stderr}")


if __name__ == "__main__":
    print_dep_tree()