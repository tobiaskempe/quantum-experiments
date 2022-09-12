
from sequences import sequences
from collections import defaultdict
import numpy as np

sequence = sequences[0]

# params
L = 3
L_squared = L**2
N = len(sequence)
lambs = np.array([2.0, 3.0, 3.0])
lambs += 1

D = L_squared * N

h = defaultdict(int)
J = defaultdict(int)

# HP Energy
def add_HP_terms(f1, f2, s1, s2):
  x1 = s1 * N + f1
  x2 = s2 * N + f2
  h[x1] += 0.25
  h[x2] += 0.25
  J[(x1, x2)] += -0.25

for f1 in range(N):
  for f2 in range(f1+2, N):
    if (sequence[f1] == 'H' and sequence[f2] == 'H'):
      for s1 in range(L_squared):
        if s1 % L != 0:
          add_HP_terms(f1, f2, s1, s1-1)
        if s1 % L != L-1:
          add_HP_terms(f1, f2, s1, s1+1)
        if int(s1 / L) != 0:
          add_HP_terms(f1, f2, s1, s1-L)
        if int(s1 / L) != L-1:
          add_HP_terms(f1, f2, s1, s1+L)

# E1
def add_E1_terms(f, s1, s2):
  x1 = s1 * N + f
  x2 = s2 * N + f
  h[x1] += -0.25 * lambs[0]
  h[x2] += -0.25 * lambs[0]
  J[(x1, x2)] += +0.25 * lambs[0]

for x in range(D):
  h[x] += 1 * lambs[0]

for f in range(N):
  for s1 in range(L_squared):
    for s2 in range(L_squared):
      add_E1_terms(f, s1, s2)

# E2
def add_E2_terms(f1, f2, s):
  x1 = s * N + f1
  x2 = s * N + f2
  h[x1] += -0.125 * lambs[1]
  h[x2] += -0.125 * lambs[1]
  J[(x1, x2)] += +0.125 * lambs[1]

for f1 in range(N):
  for f2 in range(N):
    if f1 != f2:
      for s in range(L_squared):
        add_E2_terms(f1, f2, s)
      
# E3
def lattice_neighbors(s1, s2):
  if s1 % L != 0 and s2 == s1 - 1:
    return True
  if s1 % L != L-1 and s2 == s1 + 1: 
    return True
  if int(s1 / L) != 0 and s2 == s1 - L:
    return True
  if int(s1 / L) != L-1 and s2 == s1 + L:
    return True
  return False

def add_E3_terms(f1, f2, s1, s2):
  x1 = s1 * N + f1
  x2 = s2 * N + f2
  h[x1] += -0.25 * lambs[2]
  h[x2] += -0.25 * lambs[2]
  J[(x1, x2)] += 0.25 * lambs[2]

for f2 in range(1, N):
  f1 = f2 - 1
  for s1 in range(L_squared):
    for s2 in range(L_squared):
      if not lattice_neighbors(s1, s2):
        add_E3_terms(f1, f2, s1, s2)

if __name__ == '__main__':
  print(h)
  print(J)
  print(D)
  print(len(h))
  print(len(J))
