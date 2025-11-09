import numpy as np
import matplotlib.pyplot as plt

def z(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = z(X, Y)

fig = plt.figure(figsize = (10, 6))
ax = fig.add_subplot(111, projection = '3d')
surf = ax.plot_surface(X, Y, Z, cmap = 'viridis', edgecolor = 'none')
fig.colorbar(surf, ax = ax, shrink = 0.5, aspect = 10)
ax.set_title('z = sin(sqrt(x^2 + y^2))')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
