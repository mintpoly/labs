import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4, 5]
y = [0.99, 0.49, 0.35, 0.253, 0.18]
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
v, p = np.polyfit(x, y, deg=1, cov=True)
plt.grid()
plt.plot(x, np.poly1d(p))
plt.show()

