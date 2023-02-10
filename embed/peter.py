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
  #print(sampler.properties['topology'])
  _, T, _ = sampler.structure

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
  

def scan_peters_marks():

  NLQ, NPQ, ACL, MCL = [], [], [], []
  for M in range(3, 13):
    NPQ_, ACL_, MCL_ = do_peter(10, M, 2)
    NPQ.append(NPQ_)
    ACL.append(ACL_)
    MCL.append(MCL_)
    NLQ.append(10*M)

  NPQ = np.array(NPQ)
  NLQ = np.array(NLQ)
  ACL = np.array(ACL)
  MCL = np.array(MCL)

  np.save('NPQ.npy', NPQ)
  np.save('NLQ.npy', NLQ)
  np.save('ACL.npy', ACL)
  np.save('MCL.npy', MCL)

def scan_peters_nodes():

  NLQ, NPQ, ACL, MCL = [], [], [], []
  for N in range(1, 26):
    NPQ_, ACL_, MCL_ = do_peter(N, 8, 2)
    NPQ.append(NPQ_)
    ACL.append(ACL_)
    MCL.append(MCL_)
    NLQ.append(N*8)

  NPQ = np.array(NPQ)
  NLQ = np.array(NLQ)
  ACL = np.array(ACL)
  MCL = np.array(MCL)

  np.save('NPQ.npy', NPQ)
  np.save('NLQ.npy', NLQ)
  np.save('ACL.npy', ACL)
  np.save('MCL.npy', MCL)

def scan_peters_correlation():

  NLQ, NPQ, ACL, MCL = [], [], [], []
  for c in range(1, 11):
    NPQ_, ACL_, MCL_ = do_peter(8, 7, c)
    NPQ.append(NPQ_)
    ACL.append(ACL_)
    MCL.append(MCL_)
    NLQ.append(7*8)

  NPQ = np.array(NPQ)
  NLQ = np.array(NLQ)
  ACL = np.array(ACL)
  MCL = np.array(MCL)

  np.save('NPQ.npy', NPQ)
  np.save('NLQ.npy', NLQ)
  np.save('ACL.npy', ACL)
  np.save('MCL.npy', MCL)


if __name__ == '__main__':
  #do_peter(25, 12, 5)
  #do_peter(10, 5, 2)

  #scan_peters_nodes()
  scan_peters_correlation()
