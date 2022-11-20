
import numpy as np

v = np.array([
  [1, -1, -1, 1, 1],
  [-1, 0, -1, 0, 0],
  [0, 0, 0, -1, 0],
  [0, 1, 0, 0, 1],
])

energies = np.zeros(2**len(v))
