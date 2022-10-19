
import numpy as np
import matplotlib.pyplot as plt
from problem_to_ising import problem_to_ising
from generate_problem import generate_problem


def ac_ising(h, J, verbose=True):

  _ = h

  s = set()

  for x in J:
    s.update(set(x))

  n_vars = max(s) + 1

  n_couplings = np.zeros((n_vars, ), dtype=np.int)

  for x in J:
    if J[x] != 0:
      n_couplings[x[0]] += 1
      n_couplings[x[1]] += 1
  
  mean_couplings = np.mean(n_couplings)

  if verbose:
    print(n_couplings)
    print(mean_couplings)

    plt.figure()
    plt.title('Couplings per qubits')
    plt.xlabel('Qubit')
    plt.ylabel('Couplings')
    plt.bar(np.array(range(n_vars)) + 1, n_couplings, label='Count')
    plt.hlines([mean_couplings], 0.5, n_vars + 0.5, color='orange', label=f'Mean = {round(mean_couplings, 2)}')
    plt.legend(loc='lower right')
    plt.show()

  return n_couplings, mean_couplings


if __name__ == '__main__':

  #A = np.load('problems/problem_15_1.npy')
  A = generate_problem(472, 30, 9)
  h, J = problem_to_ising(A)
  ac_ising(h, J)

