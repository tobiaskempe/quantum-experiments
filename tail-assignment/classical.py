from collections import defaultdict
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import numpy as np
import json
import dimod

import dwave.inspector

A = np.load('problem_10_1.npy')
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

for j in range(R):
  for i in range(j):
    J[(i, j)] = 1/2 * aat[i, j]

chain_strength = 5.4
n_runs = 10

response = dimod.ExactSolver().sample_ising(h, J)
print(response)
print("Energy Reached:", response.first.energy)
print(response.first)
print(f"We have {len(response.record)} different records.")
print(response)
print("-----")
