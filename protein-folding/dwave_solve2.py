
from ising_params import h, J
import numpy as np
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import dwave.inspector

chain_strength = 20

# simulate energy
x = np.ones((36))
x[[0, 10, 22, 30]] = -1
#x[[19, 36, 53]] = -1
E = 0
for i in h:
  E += h[i] * x[i]
for i, j in J:
  E += J[(i, j)] * x[i] * x[j]
print("Energy Target:", E)

#exit(0)

n_runs = 50

sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample_ising(
  h,
  J,
  chain_strength=chain_strength,
  num_reads=n_runs,
  annealing_time=1000,
  label='Protein Folding (Ising)',
)

print("Energy Reached:", response.first.energy)
print(response.first)
print(f"We have {len(response.record)} different records.")
print(response.record)
print(response)
print("-----")
#print(json.dumps(response.info, sort_keys=True, indent=2))
#print(response.record)

dwave.inspector.show(response)
