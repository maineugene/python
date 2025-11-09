import matplotlib.pyplot as plt
import numpy as np

# claster1
x1 = np.random.normal(2, 0.5, 50)
y1 = np.random.normal(2, 0.5, 50)

# claster2
x2 = np.random.normal(5, 0.5, 50)
y2 = np.random.normal(5, 0.5, 50)

# claster3
x3 = np.random.normal(8, 0.5, 50)
y3 = np.random.normal(8, 0.5, 50)

plt.figure(figsize=(10, 6))

plt.scatter(x1, y1, color = 'red', label = 'claster 1')
plt.scatter(x2, y2, color = 'blue', label = 'claster 2')
plt.scatter(x3, y3, color = 'yellow', label = 'claster 3')

plt.title('clasters 1-3', fontsize = 14)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()



