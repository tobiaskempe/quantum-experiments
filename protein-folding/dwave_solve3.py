
from qubo_params import Q
import numpy as np
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import dwave.inspector
import dimod

print(f'len(Q): {len(Q)}')
print(max(Q.values()))
print(Q)

relative_chain_strength = 1
chain_strength = max(Q.values()) * relative_chain_strength

n_runs = 50

bqm = dimod.BQM.from_qubo(Q)
sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample(
  bqm,
  chain_strength=chain_strength,
  num_reads=n_runs,
  annealing_time=200,
  label='Protein Folding (QUBO)',
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
