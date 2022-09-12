
import numpy as np

def draw_grid(x, L, N):
  grid = np.zeros((L, L))
  for f in range(N):
    g_ = (x[f*L**2:(f+1)*L**2].reshape((L, L)) - 1) * (-0.5)
    grid += g_ * (f + 1)
  print(grid)

if __name__ == '__main__':
  x = np.ones((64))
  #x[[4, 16, 33, 53]] = -1
  x[[0, 10, 22, 30]] = -1
  #x[[8, 32, 34, 37, 39, 54, 59]] = -1
  #x[[19, 36, 53]] = -1

  L = 3
  N = 4

  draw_grid(x, L, N)
