
import numpy as np
from scipy.sparse import coo_array, kron
from collections import defaultdict
from solver import lanczos_iteration

A = np.load('problem_10_1.npy')
F = A.shape[1]
R = A.shape[0]
lamb = 0

c = np.zeros((R))

# compute helper variables
b = np.ones((F))
aat = A.dot(A.T)

h = defaultdict(int)
J = defaultdict(int)

for (i, occs) in enumerate(aat):
  h[i] = 1/2 * np.sum(occs) - np.sum(A[i]) + 1/2 * lamb * c[i]

for j in range(R):
  for i in range(j):
    J[(i, j)] = 1/2 * aat[i, j]

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

hamiltonian = 0.5 * all_x + 0.5 * all_z

ones = np.ones((n_dims))

Q, T = lanczos_iteration(hamiltonian, ones, 50)

#Tk = Q.T.dot(hamiltonian).dot(Q)
Tk = (Q.T @ hamiltonian) @ Q
print('Tk:', Tk)

ut, vt = np.linalg.eigh(Tk)
ut = np.sort(ut)
print('approximation:', ut)

#print(hamiltonian.toarray)
u, v = np.linalg.eigh(hamiltonian.toarray())
u = np.sort(u)
print('exact:', u)

diffs = u[:len(ut)] - ut
print('diffs:', diffs.T)

