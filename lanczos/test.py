import numpy as np
from solver import lanczos_iteration

#M = np.array([[1, 1, 1], [1, 4, 3], [1, 3, 1]])
#b = np.array([1, 1, 1])
#n = 2
#M = np.array([[1, 1, 1, 1], [1, 2, 3, 1], [1, 3, 1, 1], [1, 1, 1, 4]]).T
#b = np.array([1, 1, 1, 1])
#n = 3
d = 100
M = np.random.rand(d, d)
M = M + M.conjugate().T
b = np.zeros(d)
b[0] = 1
n = 20

#print('M:', M)

Q, T = lanczos_iteration(M, b, n)

#print('Q:', Q)
#print('T:', T)

Tk = np.dot(np.dot(Q.T, M), Q)
#print('Tk:', Tk)

ut, vt = np.linalg.eigh(Tk)
ut = np.sort(ut)
print('approximation:', ut)

u, v = np.linalg.eig(M)
u = np.sort(u)
print('exact:', u[:n+1])

diffs = u[:len(ut)] - ut
print('diffs:', diffs.T)
