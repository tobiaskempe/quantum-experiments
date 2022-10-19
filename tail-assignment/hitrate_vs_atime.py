
import numpy as np
import matplotlib.pyplot as plt

x_lin = np.linspace(0, 3, 10)
x = np.power(10, x_lin)
y_2000q = np.array([0, 0, 0, 0, 0.19, 0.02, 0.22, 0.22, 0.56, 0.48])
y_advantage = np.array([0.03, 0.05, 0.19, 0.12, 0.35, 0.29, 0.69, 0.67, 0.64, 0.73])

plt.figure() #figsize=(6, 3))
plt.title('Influence of annealing time (small sample set)')
plt.xlabel(f'Annealing time $[\mu s]$')
plt.xscale('log')
plt.ylabel('Success rate')
plt.plot(x, y_2000q, '-o', color='green', label='2000Q')
plt.plot(x, y_advantage, '-o', color='blue', label='Advantage')
plt.legend()
plt.grid()
plt.show()
