import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.sin(x) * np.cos(x)

plt.figure(figsize=(12, 6))

plt.plot(x, y)

plt.title("y = sin(x) * cos(x)")
plt.xlabel("x")
plt.ylabel("y")

plt.tight_layout()

plt.show()