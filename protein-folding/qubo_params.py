
from sequences import sequences
from collections import defaultdict
import numpy as np
import time

sequence = sequences[0]
print(time.time())

# params
L = 2
L_squared = L**2
N = len(sequence)
lambs = np.array([1.0, 1.0, 1.0])

D = L_squared * N

Q = defaultdict(int)

# HP Energy
if True:
  def add_HP_terms(f1, f2, s1, s2):
    x = np.sort(np.array([s1 * N + f1, s2 * N + f2]))
    Q[(x[0], x[1])] += -1
    #h[x1] += 0.25
    #h[x2] += 0.25
    #J[(x1, x2)] += -0.25

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

# E1: Each bead on 1 lattice site
for f in range(N):
  for s1 in range(L_squared):
    x = s1 * N + f
    Q[(x, x)] += - 2 * lambs[0]
    for s2 in range(L_squared):
      x = np.sort(np.array([s1 * N + f, s2 * N + f]))
      Q[(x[0], x[1])] += 1 * lambs[0]

# E2: Each lattice site max 1 bead
for f1 in range(N):
  for f2 in range(N):
    if f1 != f2:
      for s in range(L_squared):
        x = np.sort(np.array([s * N + f1, s * N + f2]))
        Q[(x[0], x[1])] += +0.5 * lambs[1]
      
# E3: Connecting beads to a chain
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


for f2 in range(1, N):
  f1 = f2 - 1
  for s1 in range(L_squared):
    for s2 in range(L_squared):
      if not lattice_neighbors(s1, s2):
        x = np.sort(np.array([s1 * N + f1, s2 * N + f2]))
        Q[(x[0], x[1])] += 0.25 * lambs[2]

if __name__ == '__main__':
  print(Q)
  print(D)
  print(len(Q))
