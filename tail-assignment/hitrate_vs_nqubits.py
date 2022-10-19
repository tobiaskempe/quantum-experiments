
import numpy as np
import matplotlib.pyplot as plt

x = np.array([40, 50, 60, 80, 100, 120])
y_2000q_dummy = np.array([1, 1, 0.1, 0.05, 0.01, 0.001])
y_2000q = y_2000q_dummy
y_advantage_dummy = np.array([0.9, 0.9, 0.1, 0.05, 0.01, 0.001]) + 0.1
y_advantage = np.array([0.33])

plt.figure()
plt.title('this is a title')
plt.xlabel('Logical qubits')
plt.ylabel('Success rate')
plt.yscale('log')
plt.scatter(x, y_2000q, color='green', label='2000Q')
plt.scatter(x, y_advantage, color='blue', label='Advantage')
plt.legend()
plt.show()
