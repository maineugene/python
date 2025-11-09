#13 вариант
import numpy as np, matplotlib.pyplot as plt

def func1(x):
    return 2 * (np.sin(3 * np.pi - 2 * x)) ** 2 * (np.cos(5 * np.pi + 2 * x)) ** 2
def func2(x):
    return 1/4 - 1/4 * np.sin(5/2 * np.pi - 8 * x)

X = np.linspace(0, 2 * np.pi, 100)
fig, ax1 = plt.subplots(figsize = (12,8))

Y_0 = func1(X)
Y_1 = func2(X)

ax1.set_xlabel("x, радианы")
ax1.set_ylabel("y1", color = "blue",fontsize = 10)
line1 = ax1.plot(X, Y_0, color ="blue", linewidth = 2, label ="y1")
ax1.grid(True, alpha=0.3)

ax2 = ax1.twinx()
ax2.set_ylabel("y2", color = "red",fontsize = 10)
line2 = ax2.plot(X, Y_1, color="red", linewidth=2, linestyle='--', label='y2')
ax2.tick_params(axis='y', labelcolor="red")

# Объединяем легенды с обеих осей
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right', fontsize=10)

# аннотации
ax1.annotate('Максимум y1', xy=(1.57, max(Y_0)), xytext=(2, max(Y_0) + 0.1),
             arrowprops=dict(facecolor='blue', alpha=0.7),
             fontsize=9, color='blue')

ax2.annotate('Минимум y2', xy=(0.8, min(Y_1)), xytext=(1.5, min(Y_1) - 0.1),
             arrowprops=dict(facecolor='red', alpha=0.7),
             fontsize=9, color='red')

plt.title("Graphics of 2 functions(y1 and y2)")
plt.show()
