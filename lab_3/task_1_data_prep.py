# task_1_data_prep.py
# Лабораторна робота №3. Завдання 1. Підготовка даних та базової моделі

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def prepare_wine_data(test_size=0.3, random_state=42):
    """
    Завантажує набір даних Wine та розділяє його на навчальну і тестову вибірки.
    """
    data = load_wine()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    return X_train, X_test, y_train, y_test


def evaluate_baseline_model(X_train, X_test, y_train, y_test, random_state=42):
    """
    Оцінює точність (Accuracy) базової моделі Random Forest за замовчуванням.
    """
    base_model = RandomForestClassifier(random_state=random_state)
    base_model.fit(X_train, y_train)
    predictions = base_model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return base_model, accuracy



if __name__ == "__main__":
    X_train, X_test, y_train, y_test = prepare_wine_data()
    _, base_acc = evaluate_baseline_model(X_train, X_test, y_train, y_test)

    print("--- Дані завантажено успішно ---")
    print(f"Навчальна вибірка: {X_train.shape[0]} зразків")
    print(f"Тестова вибірка: {X_test.shape[0]} зразків")
    print(f"Базова модель (Random Forest Default) Accuracy: {base_acc:.4f}")