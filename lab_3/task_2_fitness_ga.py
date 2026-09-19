# task_2_fitness_ga.py
# Лабораторна робота №3. Завдання 2. Формування хромосоми та Fitness-функції

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from task_1_data_prep import prepare_wine_data


def create_fitness_function(X_train, y_train, X_test, y_test):
    """
    Створює та повертає функцію пристосованості (Fitness Function) для PyGAD.
    """

    def fitness_func(ga_instance, solution, solution_idx):
        n_estimators = int(solution[0])
        max_depth = int(solution[1])
        min_samples_split = int(solution[2])
        criterion = "gini" if int(solution[3]) == 0 else "entropy"

        # Фіксуємо n_jobs=1, щоб не блокувати процес паралелізацією joblib
        model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            criterion=criterion,
            n_jobs=1,
            random_state=42
        )
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        return accuracy_score(y_test, predictions)

    return fitness_func


# --- БЛОК ДЛЯ ТЕСТОВОГО ЗАПУСКУ ФАЙЛУ НАПРЯМУ ---
if __name__ == "__main__":
    X_train, X_test, y_train, y_test = prepare_wine_data()
    fitness_func = create_fitness_function(X_train, y_train, X_test, y_test)

    test_solution = [150, 10, 4, 0]
    test_fitness = fitness_func(None, test_solution, 0)
    print("--- Тестова оцінка функції пристосованості ---")
    print(f"Хромосома: {test_solution}")
    print(f"Отримане значення Fitness (Accuracy): {test_fitness:.4f}")