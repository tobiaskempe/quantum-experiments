
import numpy as np
from collections import defaultdict

def problem_to_ising(A, verbose=False):
  if verbose:
    print('Verbose not implemented.')
  
  F = A.shape[1]
  R = A.shape[0]
  lamb = 0

  c = np.zeros((R))

  # compute helper variables
  b = np.ones((F))
  aat = A.dot(A.T)

  # formulate as ising parameters
  h = defaultdict(int)
  J = defaultdict(int)
  strengths = []

  for (i, occs) in enumerate(aat):
    h[i] = 1/2 * np.sum(occs) - np.sum(A[i]) + 1/2 * lamb * c[i]

  for j in range(R):
    for i in range(j):
      J[(i, j)] = 1/2 * aat[i, j]

  return h, J
