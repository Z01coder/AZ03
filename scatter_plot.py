import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x = np.random.rand(50)
y = np.random.rand(50)

# Построение диаграммы рассеяния
plt.scatter(x, y)

# Настройка графика
plt.title("Диаграмма рассеяния")
plt.xlabel("X")
plt.ylabel("Y")

plt.grid(True)
plt.show()
