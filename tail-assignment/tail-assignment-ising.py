from collections import defaultdict
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import numpy as np
import json

import dwave.inspector

A = np.load('problem_40_1.npy')
#print(A)

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
  strengths.append(h[i])

for j in range(R):
  for i in range(j):
    J[(i, j)] = 1/2 * aat[i, j]
    strengths.append(J[(i, j)])

max_strength = max(strengths)
relative_chain_strength = 0.3
chain_strength = max_strength * relative_chain_strength
print(f"chain strength: {chain_strength}")

# simulate energy
x = np.ones((R))
x[9:] = -1
E = 0
for i in h:
  E += h[i] * x[i]
for i, j in J:
  E += J[(i, j)] * x[i] * x[j]
print("Energy Target:", E)

#chain_strength = 40
n_runs = 10

sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample_ising(
  h,
  J,
  chain_strength=chain_strength,
  num_reads=n_runs,
  annealing_time=100,
  label='Tail Assignment',
)

print("Energy Reached:", response.first.energy)
print(response.first)
print(f"We have {len(response.record)} different records.")
print(response)
print("-----")
#print(json.dumps(response.info, sort_keys=True, indent=2))
#print(response.record)

dwave.inspector.show(response)
