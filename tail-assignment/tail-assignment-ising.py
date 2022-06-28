from collections import defaultdict
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import numpy as np

F = 472
R = 30
lamb = 1

# defines the 2SAT instance
A = np.empty((R, F))
#A = np.array([
  #[1, -1, -1, 1, 1],
  #[-1, 0, -1, 0, 0],
  #[0, 0, 0, -1, 0],
  #[0, 1, 0, 0, 1],
#])
c = np.empty((R))

# compute helper variables
b = np.ones((F))
aat = A.dot(A.T)

# formulate as ising parameters
h = defaultdict(int)
J = defaultdict(int)

for (i, occs) in enumerate(aat):
  h[i] = 1/2 * np.sum(occs) - np.sum(A[i]) + 1/2 * lamb * c[i]

for j in range(R):
  for i in range(j):
    J[(i, j)] = 1/2 * aat[i, j]

print(h)
print(J)

chain_strength = 2
n_runs = 100

sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample_ising(
  h,
  J,
  chain_strength=chain_strength,
  num_reads=n_runs,
  label='2SAT Ising',
)

print(response)
print(response.first)
print(response.info)
print(response.record)
