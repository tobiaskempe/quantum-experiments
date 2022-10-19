
import numpy as np
import matplotlib.pyplot as plt

x_4 = np.array([30, 166])
y_4 = np.array([0.38, 0.04])
x_6 = np.array([325])
y_6 = np.array([0.0025])

plt.figure() #figsize=(4, 3))
#plt.title('')
plt.xlabel('Physical qubits', fontsize=16)
plt.ylabel('Success rate', fontsize=16)
plt.yscale('log')
#plt.rcParams.update({'font.size': 22})
plt.scatter([30], [0.38], color='green', marker='o', label='N=4, L=2, Adv')
plt.scatter([28], [0.83], color='blue', marker='o', label='N=4, L=2, Adv2')
plt.scatter([166], [0.04], color='green', marker='s', label='N=4, L=3, Adv')
plt.scatter([119], [0.24], color='blue', marker='s', label='N=4, L=3, Adv2')
plt.scatter([325], [0.0025], color='green', marker='D', label='N=6, L=3, Adv')
plt.scatter([243], [0.015], color='blue', marker='D', label='N=6, L=3, Adv2')
plt.grid()
plt.legend()
plt.show()
