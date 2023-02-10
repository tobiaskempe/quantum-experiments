import matplotlib.pyplot as plt
import numpy as np

NLQ = np.load('NLQ.npy')
NPQ = np.load('NPQ.npy')

x = np.linspace(1, 25, 25)

print(NLQ)
print(NPQ)
print(x)

plt.figure()
plt.title('# of qubits vs. # of nodes (for M=8 marks)')
plt.plot(x, NPQ, label='Physical')
plt.plot(x, NLQ, label='Logical')
plt.xlabel('# of nodes')
plt.ylabel('# of qubits')
plt.grid()
plt.legend()
plt.savefig('Qubits.pdf')



ACL = np.load('ACL.npy')
MCL = np.load('MCL.npy')

print(ACL)
print(MCL)



plt.figure()
plt.title('chain lengths vs. # of nodes (for M=8 marks)')
plt.plot(x, ACL, label='Average')
plt.plot(x, MCL, label='Maximum')
plt.xlabel('# of nodes')
plt.ylabel('chain length')
plt.grid()
plt.legend()
plt.savefig('ChainLengths.pdf')
