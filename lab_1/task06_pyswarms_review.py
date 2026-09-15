# task06_pyswarms_review
# Лаб 1. Завдання 6. Аналіз програмних прикладів. Офіційний приклад з документації PySwarms: Training a Neural Network
# https://pyswarms.readthedocs.io/en/latest/examples/usecases/train_neural_network.html#Neural-network-architecture

import time
import numpy as np
from sklearn.datasets import load_iris
import pyswarms as ps

# 1. Завантаження датасету Iris
data = load_iris()
X = data.data
y = data.target

# Архітектура нейромережі: 4 входи -> 20 прихованих нейронів -> 3 класи
n_inputs = 4
n_hidden = 20
n_classes = 3
num_samples = 150


# 2. Обчислення логітів (розгортання вектора ваг частки назад у матриці W1, b1, W2, b2)
def logits_function(p):
    W1 = p[0:80].reshape((n_inputs, n_hidden))
    b1 = p[80:100].reshape((n_hidden,))
    W2 = p[100:160].reshape((n_hidden, n_classes))
    b2 = p[160:163].reshape((n_classes,))

    # Пряме поширення (Forward Propagation)
    z1 = X.dot(W1) + b1
    a1 = np.tanh(z1)
    logits = a1.dot(W2) + b2
    return logits


# 3. Цільова функція обчислення похибки (Negative Log-Likelihood Loss)
def forward_prop(params):
    logits = logits_function(params)
    exp_scores = np.exp(logits)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

    corect_logprobs = -np.log(probs[range(num_samples), y])
    loss = np.sum(corect_logprobs) / num_samples
    return loss


def f(x):
    n_particles = x.shape[0]
    j = [forward_prop(x[i]) for i in range(n_particles)]
    return np.array(j)


# 4. Перевірка точності класифікації з найкращою позицією часток
def predict(pos):
    logits = logits_function(pos)
    return np.argmax(logits, axis=1)


# 5. Функція тестування продуктивності та запуску оптимізації
def run_performance_test():
    options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
    dimensions = (n_inputs * n_hidden) + (n_hidden * n_classes) + n_hidden + n_classes  # 163 виміри

    print("=== Запуск навчання нейромережі через PySwarms (GlobalBestPSO) ===")
    start_time = time.perf_counter()

    optimizer = ps.single.GlobalBestPSO(n_particles=100, dimensions=dimensions, options=options)
    cost, pos = optimizer.optimize(f, iters=1000)

    elapsed_time = time.perf_counter() - start_time

    # Обчислення точності
    y_pred = predict(pos)
    accuracy = (y_pred == y).mean()
    correct_count = np.sum(y_pred == y)

    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТИ ТЕСТУВАННЯ ПРОДУКТИВНОСТІ:")
    print("=" * 50)
    print(f"Час виконання оптимізації : {elapsed_time:.2f} сек")
    print(f"Найкраща вартість (Best Cost) : {cost:.6f}")
    print(f"Правильно класифіковано    : {correct_count} з {num_samples}")
    print(f"Точність (Accuracy)           : {accuracy * 100:.2f}%")
    print("=" * 50)


if __name__ == '__main__':
    run_performance_test()