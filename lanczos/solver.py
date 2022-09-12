import numpy as np

def lanczos_iteration(M: np.ndarray, b: np.ndarray, n: int):
  M_size = M.shape[0]

  T = np.zeros((n + 1, n))
  Q = np.zeros((M_size, n + 1))

  # normalizes input vector
  Q[:, 0] = (b / np.linalg.norm(b)).T

  for i in range(n):

    # generates a new vector by applying M
    v = M.dot(Q[:, i])

    # stores similarity between current and previous vectors in (diagonal) T matrix
    # (supposedly, we're guaranteed to get a real value here)
    T[i, i] = np.dot(Q[:, i].conjugate(), v)

    # TODO I don't really understand, what's happening here!
    # We somehow adjust our "candidate vector"...
    # We seem to compute a vector which spans a new dimension of the Krylov subspace by being orthogonal to the previous vectors.
    v = (v.T - b[i-1] * Q[:, i-1] - T[i, i] * Q[:, i]).T

    T[i + 1, i] = np.linalg.norm(v)
    b[i] = T[i + 1, i]

    epsilon = 1e-12
    
    if T[i + 1, i] > epsilon:
      Q[:, i+1] = (v / T[i + 1, i]).T
    else:
      return Q, T

  return Q, T
