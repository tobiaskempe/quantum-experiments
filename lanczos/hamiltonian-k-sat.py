
import numpy as np
from scipy.sparse import coo_array, kron
from collections import defaultdict
from solver import lanczos_iteration
import lanczos as lz
import matplotlib.pyplot as plt

from ..two_sat.three_sat_ising import h, J

pauli_0 = coo_array(([1, 1], ((0, 1), (0, 1))), shape=(2, 2))
pauli_x = coo_array(([1, 1], ((0, 1), (1, 0))), shape=(2, 2))
pauli_y = coo_array(([-1j, 1j], ((0, 1), (1, 0))), shape=(2, 2))
pauli_z = coo_array(([1, -1], ((0, 1), (0, 1))), shape=(2, 2))

n_qubits = 10
n_dims = 2 ** n_qubits

all_x = coo_array(([0], ((0, ), (0, ))), shape=(n_dims, n_dims))
for i in range(n_qubits):
  x_i = pauli_x.copy()
  for _ in range(0, i):
    x_i = kron(pauli_0, x_i)
  for _ in range(i+1, n_qubits):
    x_i = kron(x_i, pauli_0)
  all_x += x_i

all_z = coo_array(([0], ((0, ), (0, ))), shape=(n_dims, n_dims))
for i, h_i in h.items():
  z_i = pauli_z.copy()
  for _ in range(0, i):
    z_i = kron(pauli_0, z_i)
  for _ in range(i+1, n_qubits):
    z_i = kron(z_i, pauli_0)
  all_z += h_i * z_i

for x, J_ij in J.items():
  i, j = x
  zz_ij = pauli_z.copy()
  for _ in range(0, i):
    zz_ij = kron(pauli_0, zz_ij)
  for _ in range(i+1, j):
    zz_ij = kron(zz_ij, pauli_0)
  zz_ij = kron(zz_ij, pauli_z)
  for _ in range(j+1, n_qubits):
    zz_ij = kron(zz_ij, pauli_0)
  all_z += J_ij * zz_ij

steps = 10
s_series = np.linspace(0, 1, steps)
B_series = s_series.copy()
A_series = 1 - B_series

iterations = 10

approximations = np.zeros((iterations + 1, steps))
exacts = np.zeros((iterations + 1, steps))
diffs = np.zeros((iterations + 1, steps))

for i in range(steps):

  hamiltonian = A_series[i] * all_x + B_series[i] * all_z

  ones = np.random.uniform(low=0.5, high=1.0, size=(n_dims,))

  Q, T = lanczos_iteration(hamiltonian, ones, iterations)

  Tk = (Q.T @ hamiltonian) @ Q

  ut, vt = np.linalg.eigh(Tk)
  ut = np.sort(ut)
  approximations[:, i] = ut
  #print(len(ut))
  #print('approximation:', ut)

  #print(hamiltonian.toarray)
  u, v = np.linalg.eigh(hamiltonian.toarray())
  u = np.sort(u)
  exacts[:, i] = u[:(iterations+1)]
  #print('exact:', u)
  if i==0:
    print('approximation:', ut)
    print('exact:', u)

  #diffs = u[:len(ut)] - ut
  #print('diffs:', diffs.T)
  print(f'Simulated step {(i+1)}.')

diffs = exacts - approximations
gaps = approximations[1, :] - approximations[0, :]
minimum_gap = np.min(gaps)
print(f'Minimum energy gap: {minimum_gap}.')

plt.figure()
plt.xlabel('Time variable $s(t)$')
plt.ylabel('Energy eigenstates of $H(t)$')
plt.plot(s_series, approximations[0], color="blue", label="Ground state")
plt.plot(s_series, approximations[1], color="green", label="1st excited state")
plt.plot(s_series, exacts[0], linestyle='None', marker="x", color="blue")
plt.plot(s_series, exacts[1], linestyle='None', marker="x", color="green")
plt.legend()
plt.show()

