import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(10, 10)

plt.figure(figsize = (10, 6))
plt.imshow(data, cmap='viridis')
plt.colorbar()
plt.title('Тепловая карта случайной матрицы 10x10')
plt.xlabel('Столбцы')
plt.ylabel('Строки')
plt.show()
