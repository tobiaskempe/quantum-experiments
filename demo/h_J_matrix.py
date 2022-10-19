
import numpy as np

def from_hJN(h, J, N):
  hJ = np.zeros((N, N), dtype=int)
  for h_ in h:
      hJ[h_] = h[h_]
  for J_ in J:
      hJ[J_[0]-1, J_[1]-1] = J[J_]
  return hJ
