import minorminer
import networkx as nx
import dwave_networkx as dnx
import matplotlib.pyplot as plt

import numpy as np
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import dwave.inspector
import dimod
import importlib
from collections import defaultdict
import matplotlib.pyplot as plt


N_SAMPLES = 100
TOPOLOGY = 'pegasus'


def do_peter(n_nodes, n_marks, corr_length):
  print(f'do_peter({n_nodes}, {n_marks}, {corr_length})')

  means = np.load('means2.npy')
  covs = np.load('covs2.npy').T
        
  # number of marks
  M = n_marks

  # number of nucleosomes
  N = n_nodes

  # pair-wise correlation
  J = defaultdict(int)
  for n in range(N):
    for i in range(M):
      for j in range(i+1, M):
        x = n * M + i
        y = n * M + j
        J[(x, y)] = covs[i, j]
      for l in range(1, corr_length+1):
        x = n * M + i
        y = ((n + l) % N) * M + i
        J[(x, y)] = 1

  G = nx.Graph()
  G.add_edges_from(list(J.keys()))

  sampler = DWaveSampler() #solver='Advantage2_prototype1.1')
  ##print(sampler.properties['topology'])
  _, T, _ = sampler.structure
  #T = dnx.zephyr_graph(6)

  embedding = minorminer.find_embedding(G, T)

  chain_lengths = [len(c) for c in embedding.values()]
  average_chain_length = np.mean(chain_lengths)
  maximum_chain_length = np.max(chain_lengths)

  physical_qubits = set()
  for chain in embedding.values():
    physical_qubits.update(set(chain))

  n_logical_qubits = N * M
  n_physical_qubits = len(physical_qubits)

  #print(n_logical_qubits)
  #print(n_physical_qubits)
  
  #plt.figure()
  #nx.draw(G)
  #plt.show()
  
  return n_physical_qubits, average_chain_length, maximum_chain_length
  

def scan_peters_marks(take_existing=False):
  
  if take_existing:
    NPQs = np.load(f'marks/{TOPOLOGY}/NPQ.npy').tolist()
    NLQs = np.load(f'marks/{TOPOLOGY}/NLQ.npy').tolist()
    ACLs = np.load(f'marks/{TOPOLOGY}/ACL.npy').tolist()
    MCLs = np.load(f'marks/{TOPOLOGY}/MCL.npy').tolist()
  else:
    NLQs, NPQs, ACLs, MCLs = [], [], [], []
  
  for i_samples in range(len(NPQs), N_SAMPLES):
    print(i_samples+1)
    NLQ, NPQ, ACL, MCL = [], [], [], []
    for M in range(3, 13):
      NPQ_, ACL_, MCL_ = do_peter(10, M, 2)
      NPQ.append(NPQ_)
      ACL.append(ACL_)
      MCL.append(MCL_)
      NLQ.append(10*M)

    NPQs.append(np.array(NPQ))
    NLQs.append(np.array(NLQ))
    ACLs.append(np.array(ACL))
    MCLs.append(np.array(MCL))

    print(TOPOLOGY)
    print(np.array(NPQs))
    np.save(f'marks/{TOPOLOGY}/NPQ.npy', np.array(NPQs))
    np.save(f'marks/{TOPOLOGY}/NLQ.npy', np.array(NLQs))
    np.save(f'marks/{TOPOLOGY}/ACL.npy', np.array(ACLs))
    np.save(f'marks/{TOPOLOGY}/MCL.npy', np.array(MCLs))

def scan_peters_nodes(take_existing=False):
  
  if take_existing:
    NPQs = np.load(f'nodes/{TOPOLOGY}/NPQ.npy').tolist()
    NLQs = np.load(f'nodes/{TOPOLOGY}/NLQ.npy').tolist()
    ACLs = np.load(f'nodes/{TOPOLOGY}/ACL.npy').tolist()
    MCLs = np.load(f'nodes/{TOPOLOGY}/MCL.npy').tolist()
  else:
    NLQs, NPQs, ACLs, MCLs = [], [], [], []
  
  for i_samples in range(len(NPQs), N_SAMPLES):
    print(i_samples+1)
    NLQ, NPQ, ACL, MCL = [], [], [], []
    for N in range(1, 26):
      NPQ_, ACL_, MCL_ = do_peter(N, 8, 2)
      NPQ.append(NPQ_)
      ACL.append(ACL_)
      MCL.append(MCL_)
      NLQ.append(N*8)

    NPQs.append(np.array(NPQ))
    NLQs.append(np.array(NLQ))
    ACLs.append(np.array(ACL))
    MCLs.append(np.array(MCL))

    print(TOPOLOGY)
    print(np.array(NPQs))
    np.save(f'nodes/{TOPOLOGY}/NPQ.npy', np.array(NPQs))
    np.save(f'nodes/{TOPOLOGY}/NLQ.npy', np.array(NLQs))
    np.save(f'nodes/{TOPOLOGY}/ACL.npy', np.array(ACLs))
    np.save(f'nodes/{TOPOLOGY}/MCL.npy', np.array(MCLs))

def scan_peters_correlation(take_existing=False):
  
  if take_existing:
    NPQs = np.load(f'correlation/{TOPOLOGY}/NPQ.npy').tolist()
    NLQs = np.load(f'correlation/{TOPOLOGY}/NLQ.npy').tolist()
    ACLs = np.load(f'correlation/{TOPOLOGY}/ACL.npy').tolist()
    MCLs = np.load(f'correlation/{TOPOLOGY}/MCL.npy').tolist()
  else:
    NLQs, NPQs, ACLs, MCLs = [], [], [], []
  
  for i_samples in range(len(NPQs), N_SAMPLES):
    print(i_samples+1)
    NLQ, NPQ, ACL, MCL = [], [], [], []
    for c in range(1, 11):
      NPQ_, ACL_, MCL_ = do_peter(8, 7, c)
      NPQ.append(NPQ_)
      ACL.append(ACL_)
      MCL.append(MCL_)
      NLQ.append(7*8)

    NPQs.append(np.array(NPQ))
    NLQs.append(np.array(NLQ))
    ACLs.append(np.array(ACL))
    MCLs.append(np.array(MCL))

    print(TOPOLOGY)
    print(np.array(NPQs))
    np.save(f'correlation/{TOPOLOGY}/NPQ.npy', np.array(NPQs))
    np.save(f'correlation/{TOPOLOGY}/NLQ.npy', np.array(NLQs))
    np.save(f'correlation/{TOPOLOGY}/ACL.npy', np.array(ACLs))
    np.save(f'correlation/{TOPOLOGY}/MCL.npy', np.array(MCLs))


if __name__ == '__main__':
  #scan_peters_marks(True)
  scan_peters_nodes(True)
  #scan_peters_correlation(True)
