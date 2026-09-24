import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

plt.figure(figsize=(6,6), facecolor="black")
plt.plot(x, y, color="#8B0000", linewidth=2)

plt.axis("equal")
plt.axis("off")

plt.title("ARSENIA <33", fontsize=20, color="white")

plt.show()