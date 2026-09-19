# task_3_experiments.py
# Лабораторна робота №3. Завдання 3. Проведення 3 експериментів із PyGAD

import pygad
from task_1_data_prep import prepare_wine_data
from task_2_fitness_ga import create_fitness_function


def run_single_experiment(generations, fitness_func, show_info=True):
    """
    Запускає один експеримент генетичного алгоритму з заданою кількістю поколінь.
    """
    gene_space = [
        range(10, 301),
        range(2, 21),
        range(2, 21),
        [0, 1]
    ]

    # Функція для виводу прогресу виконання
    def callback_generation(ga_inst):
        if ga_inst.generations_completed % 10 == 0 or ga_inst.generations_completed == 1:
            print(
                f"  [Прогрес] Покоління {ga_inst.generations_completed}/{generations} | Кращий Fitness: {ga_inst.best_solution()[1]:.4f}")

    print(f"\n>>> Запуск експерименту на {generations} поколінь...")

    ga_instance = pygad.GA(
        num_generations=generations,
        sol_per_pop=20,
        num_genes=4,
        gene_space=gene_space,
        num_parents_mating=10,
        fitness_func=fitness_func,
        parent_selection_type="tournament",
        crossover_type="single_point",
        mutation_type="random",
        mutation_probability=0.10,
        crossover_probability=0.80,
        on_generation=callback_generation,
        suppress_warnings=True,
        random_seed=42
    )

    ga_instance.run()

    solution, fitness, _ = ga_instance.best_solution()

    result = {
        "generations": generations,
        "n_estimators": int(solution[0]),
        "max_depth": int(solution[1]),
        "min_samples_split": int(solution[2]),
        "criterion": "gini" if int(solution[3]) == 0 else "entropy",
        "accuracy": fitness,
        "fitness_history": ga_instance.best_solutions_fitness
    }

    if show_info:
        print(f"=== Завершено ({generations} поколінь) ===")
        print(f"n_estimators: {result['n_estimators']}")
        print(f"max_depth: {result['max_depth']}")
        print(f"min_samples_split: {result['min_samples_split']}")
        print(f"criterion: {result['criterion']}")
        print(f"Accuracy (Fitness): {result['accuracy']:.4f}\n")

    return result


def run_all_experiments(experiments_generations=[20, 50, 100]):
    """
    Запускає серію з трьох експериментів.
    """
    X_train, X_test, y_train, y_test = prepare_wine_data()
    fitness_func = create_fitness_function(X_train, y_train, X_test, y_test)

    results = []
    for gens in experiments_generations:
        res = run_single_experiment(gens, fitness_func, show_info=True)
        results.append(res)

    return results


# --- БЛОК ДЛЯ ТЕСТОВОГО ЗАПУСКУ ФАЙЛУ НАПРЯМУ ---
if __name__ == "__main__":
    results = run_all_experiments()