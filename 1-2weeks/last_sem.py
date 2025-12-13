import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
n = 100
X = np.linspace(-3, 3, n).reshape(-1, 1)
true_w = np.array([3.0])
true_b = 2.0
noise = np.random.normal(0, 1.0, size=(n, ))
y = (X[:, 0] * true_w[0] + true_b + noise)

# Сделаем матрицу X с единичным столбцом для b
X_design = np.hstack([X, np.ones((n, 1))])  # [x, 1] — последний столбец для смещения

print("Форма X_design:", X_design.shape)
print("Форма y:", y.shape)

plt.scatter(X, y, alpha=0.7)
plt.title("Синтетические данные для линейной регрессии")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


XtX = X_design.T @ X_design
Xty = X_design.T @ y

w_full_closed_form = np.linalg.inv(XtX) @ Xty
w_hat, b_hat = w_full_closed_form[0], w_full_closed_form[1]

print(f"Аналитическое решение: w = {w_hat:.3f}, b = {b_hat:.3f}")
print(f"Истинные параметры:   w = {true_w[0]:.3f}, b = {true_b:.3f}")

# Визуализация
x_plot = np.linspace(-3, 3, 100).reshape(-1, 1)
X_plot_design = np.hstack([x_plot, np.ones((100, 1))])
y_pred = X_plot_design @ w_full_closed_form

plt.scatter(X, y, alpha=0.5, label="данные")
plt.plot(x_plot, y_pred, label="модель (аналитически)", linewidth=2)
plt.legend()
plt.title("Линейная регрессия (аналитическое решение)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# Инициализация параметров случайно
w_gd = np.random.randn(2)  # [w, b]
lr = 0.01
num_iters = 1000

loss_history = []

for it in range(num_iters):
    # Прямой проход
    y_pred = X_design @ w_gd  # (n,) = (n, 2) @ (2,)

    # Потеря MSE
    error = y_pred - y
    loss = (error @ error) / n  # скаляр
    loss_history.append(loss)

    # Градиент по w_gd
    # dL/dw = (2/n) * X^T (X w - y)
    grad = (2.0 / n) * (X_design.T @ error)

    # Шаг градиентного спуска
    w_gd -= lr * grad

print("После градиентного спуска:")
print(f"w = {w_gd[0]:.3f}, b = {w_gd[1]:.3f}")

plt.plot(loss_history)
plt.xlabel("итерация")
plt.ylabel("MSE")
plt.title("Процесс обучения (градиентный спуск)")
plt.show()
