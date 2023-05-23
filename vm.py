from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def f(x, y):
    return y * np.sqrt(x) - 2 * y**2 - x + 14 * y

fig = plt.figure()
ax = plt.axes(projection="3d")

x = np.linspace(0, 10, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

ax.plot_surface(X, Y, Z, cmap="viridis")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

# Збільшення масштабу по осям x та y
ax.set_box_aspect([1, 1, 0.7])

# Обрахунок екстремумів
start_point = np.array([5, 0])
res = optimize.minimize(lambda p: -f(*p), start_point)
min_x, min_y = res.x
min_z = -res.fun
ax.scatter(min_x, min_y, min_z, color="red")
print(f"Мінімум функції знаходиться в точці ({min_x}, {min_y}, {min_z})")

res = optimize.minimize(lambda p: f(*p), start_point)
max_x, max_y = res.x
max_z = res.fun
ax.scatter(max_x, max_y, max_z, color="green")
print(f"Максимум функції знаходиться в точці ({max_x}, {max_y}, {max_z})")

plt.show()
