

import numpy as np
import matplotlib.pyplot as plt
from problem_to_ising import problem_to_ising
from generate_problem import generate_problem


if __name__ == '__main__':

  A = generate_problem(472, 30, 9)
  plt.figure()
  plt.imshow(A)
  plt.show()
  #h, J = problem_to_ising(A)
  #ac_ising(h, J)

