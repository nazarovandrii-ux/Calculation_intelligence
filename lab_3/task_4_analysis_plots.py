# task_4_analysis_plots.py
# Лабораторна робота №3. Завдання 4. Візуалізація та аналіз результатів

import matplotlib.pyplot as plt
from task_1_data_prep import prepare_wine_data, evaluate_baseline_model
from task_3_experiments import run_all_experiments


def plot_fitness_history(results, show_plot=True):
    """
    Будує графік зміни значення функції пристосованості (Fitness) протягом еволюції.
    """
    plt.figure(figsize=(9, 4.5))
    colors = ['blue', 'green', 'red']

    for i, res in enumerate(results):
        plt.plot(
            res["fitness_history"],
            label=f"{res['generations']} поколінь (max={res['accuracy']:.4f})",
            color=colors[i % len(colors)],
            linewidth=2
        )

    plt.title('Графік зміни Fitness протягом роботи генетичного алгоритму')
    plt.xlabel('Покоління')
    plt.ylabel('Ступінь пристосованості (Fitness / Accuracy)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='lower right')
    plt.tight_layout()

    if show_plot:
        plt.show()


def plot_accuracy_comparison(results, base_accuracy, show_plot=True):
    """
    Будує стовпчикову діаграму для порівняння Accuracy в усіх експериментах.
    """
    plt.figure(figsize=(9, 4.5))
    exp_names = [f"Експеримент {i + 1}\n({r['generations']} пок.)" for i, r in enumerate(results)]
    accuracies = [r["accuracy"] for r in results]

    bars = plt.bar(exp_names, accuracies, color=['#4C72B0', '#55A868', '#C44E52'], width=0.5)

    plt.axhline(
        y=base_accuracy,
        color='black',
        linestyle='--',
        linewidth=1.5,
        label=f'Базова модель (Default Accuracy: {base_accuracy:.4f})'
    )

    plt.title('Порівняння точності моделей (Accuracy)')
    plt.xlabel('Експерименти')
    plt.ylabel('Точність класифікації (Accuracy)')
    plt.ylim(0.8, 1.05)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='upper left')

    for bar in bars:
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            yval + 0.005,
            f"{yval:.4f}",
            ha='center',
            va='bottom',
            fontsize=10,
            fontweight='bold'
        )

    plt.tight_layout()

    if show_plot:
        plt.show()


# --- БЛОК ДЛЯ ТЕСТОВОГО ЗАПУСКУ ФАЙЛУ НАПРЯМУ ---
if __name__ == "__main__":
    X_train, X_test, y_train, y_test = prepare_wine_data()
    _, base_acc = evaluate_baseline_model(X_train, X_test, y_train, y_test)

    results = run_all_experiments()

    plot_fitness_history(results, show_plot=True)
    plot_accuracy_comparison(results, base_acc, show_plot=True)