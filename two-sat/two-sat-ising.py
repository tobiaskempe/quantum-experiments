from collections import defaultdict
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import numpy as np

# defines the 2SAT instance
#v = np.array([
  #[1, -1, -1, 1],
  #[-1, 0, -1, 0],
  #[0, 1, 0, 1],
#])
v = np.array([
  [1, -1, -1, 1, 1],
  [-1, 0, -1, 0, 0],
  [0, 0, 0, -1, 0],
  [0, 1, 0, 0, 1],
])

# verifies that only 2-clauses exist!
for x in np.sum(v, axis=0):
  if x % 2 != 0:
    print("expression may only contain 2-clauses")
    raise Exception

h = defaultdict(int)
J = defaultdict(int)

for (j, occs) in enumerate(v):
  h[j] = - np.sum(occs)

n_vars = len(v)
for i in range(n_vars):
  for j in range(n_vars):
    J[(i, j)] = np.sum(v[i] * v[j])

print(h)
print(J)

chain_strength = 2
n_runs = 10

sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample_ising(
  h,
  J,
  chain_strength=chain_strength,
  num_reads=n_runs,
  label='Demo',
)

print(response)
#print(response.first)
#print(response.info)
#print(response.record)
#print(response.variables)
#print(response.vartype)

#print(response.aggregate())
#print(response.lowest())
#print(response.done())
