import numpy as np
from scipy.sparse import coo_array, kron

A = coo_array(([1, 2, 3], ((1, 3, 5), (2, 8, 13))), shape=(6, 14))
print(A)
print(A.toarray())

#v = np.ones((14)) * 2
v = coo_array(([2, 4, 6], ((2, 8, 13), (0, 0, 0))), shape=(14, 1))
print(v)
print(v.toarray())

x = A.dot(v)
print(x)

print('----------')



#print(pauli_x.toarray())
#print(pauli_y.toarray())

#d = kron(pauli_x, pauli_y)
#print(d)
#print(d.toarray())

#H = pauli_x.copy()

#for i in range(40):
  #print(i)
  #H = kron(H, pauli_0)

# you don't wanna do this one:
#q = np.ones((2**32))
#print('len:', len(q))
  