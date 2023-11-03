import matplotlib.pyplot as plt
import numpy as np

pegasus = {}
for x in ['marks', 'nodes', 'correlation']:
  pegasus[x] = {}
  pegasus[x]['NLQ'] = np.load(f'{x}/pegasus/NLQ.npy')
  pegasus[x]['NPQ'] = np.load(f'{x}/pegasus/NPQ.npy')
  pegasus[x]['ACL'] = np.load(f'{x}/pegasus/ACL.npy')
  pegasus[x]['MCL'] = np.load(f'{x}/pegasus/MCL.npy')

zephyr = {}
for x in ['marks', 'nodes', 'correlation']:
  zephyr[x] = {}
  zephyr[x]['NLQ'] = np.load(f'{x}/zephyr/NLQ.npy')
  zephyr[x]['NPQ'] = np.load(f'{x}/zephyr/NPQ.npy')
  zephyr[x]['ACL'] = np.load(f'{x}/zephyr/ACL.npy')
  zephyr[x]['MCL'] = np.load(f'{x}/zephyr/MCL.npy')

cm = 1/2.54
fs = 10
fig, ax = plt.subplots(nrows=3, ncols=3, figsize=(15*cm, 10*cm))
ax[0, 0].set_ylabel('Qubits', fontsize=fs)
ax[1, 0].set_ylabel('Avg. Chain Length', fontsize=8)
ax[2, 0].set_ylabel('Max. Chain Length', fontsize=8)
ax[2, 0].set_xlabel('Marks $M$', fontsize=fs)
ax[2, 1].set_xlabel('Nodes $N$', fontsize=fs)
ax[2, 2].set_xlabel('Correlation', fontsize=fs)

for i in range(3):
  ax[0, i].set_ylim([0, 700])

for i in range(3):
  ax[1, i].set_ylim([0, 6])

for i in range(3):
  ax[2, i].set_ylim([0, 9])

#ax[0, 1].set_yticks([])
for i in range(3):
  for j in range(1, 3):
    ax[i, j].tick_params(axis='y', which='both', labelleft=False, left=False)
  
for i in range(2):
  for j in range(3):
    ax[i, j].tick_params(axis='x', which='both', labelbottom=False, bottom=False)

lw = 2

def plot_it(ix, iy, data, c, label=None):
  m = np.mean(data, axis=0)
  s = np.std(data, axis=0)
  ax[ix, iy].plot(x, m, lw=lw, c=c, label=label)
  ax[ix, iy].fill_between(x, m-s, m+s, color=c, alpha=0.3)

x = np.linspace(3, 12, 10)
#ax[0, 0].plot(x, pegasus['marks']['NLQ'], lw=lw, c='g')
#ax[0, 0].plot(x, pegasus['marks']['NPQ'], lw=lw, c='b')
#ax[1, 0].plot(x, pegasus['marks']['ACL'], lw=lw, c='b')
#ax[2, 0].plot(x, pegasus['marks']['MCL'], lw=lw, c='b')
ax[0, 0].plot(x, pegasus['marks']['NLQ'][0], lw=lw, c='g')
#plot_it(0, 0, pegasus['marks']['NLQ'], 'g')
plot_it(0, 0, pegasus['marks']['NPQ'], 'b')
plot_it(1, 0, pegasus['marks']['ACL'], 'b')
plot_it(2, 0, pegasus['marks']['MCL'], 'b')
plot_it(0, 0, zephyr['marks']['NPQ'], 'r')
plot_it(1, 0, zephyr['marks']['ACL'], 'r')
plot_it(2, 0, zephyr['marks']['MCL'], 'r')

x = np.linspace(1, 25, 25)
ax[0, 1].plot(x, pegasus['nodes']['NLQ'][0], lw=lw, c='g')
#ax[0, 1].plot(x, pegasus['nodes']['NPQ'], lw=lw, c='b')
#ax[1, 1].plot(x, pegasus['nodes']['ACL'], lw=lw, c='b')
#ax[2, 1].plot(x, pegasus['nodes']['MCL'], lw=lw, c='b')
#ax[0, 1].plot(x, pegasus['nodes']['NLQ'][0], lw=lw, c='g')
#plot_it(0, 1, pegasus['nodes']['NLQ'], 'g')
plot_it(0, 1, pegasus['nodes']['NPQ'], 'b')
plot_it(1, 1, pegasus['nodes']['ACL'], 'b')
plot_it(2, 1, pegasus['nodes']['MCL'], 'b')
plot_it(0, 1, zephyr['nodes']['NPQ'], 'r')
plot_it(1, 1, zephyr['nodes']['ACL'], 'r')
plot_it(2, 1, zephyr['nodes']['MCL'], 'r')

x = np.linspace(1, 10, 10)
ax[0, 2].plot(x, pegasus['correlation']['NLQ'][0], lw=lw, c='g', label='Logical')
#ax[0, 2].plot(x, pegasus['correlation']['NPQ'], lw=lw, c='b', label='Pegasus')
#ax[1, 2].plot(x, pegasus['correlation']['ACL'], lw=lw, c='b')
#ax[2, 2].plot(x, pegasus['correlation']['MCL'], lw=lw, c='b')
plot_it(0, 2, pegasus['correlation']['NPQ'], 'b', label='Pegasus')
plot_it(1, 2, pegasus['correlation']['ACL'], 'b')
plot_it(2, 2, pegasus['correlation']['MCL'], 'b')
plot_it(0, 2, zephyr['correlation']['NPQ'], 'r', label='Zephyr')
plot_it(1, 2, zephyr['correlation']['ACL'], 'r')
plot_it(2, 2, zephyr['correlation']['MCL'], 'r')

ax[0, 2].legend(fontsize=8)

for i in range(3):
  for j in range(3):
    ax[i, j].grid()

plt.savefig('pegasus-scaling.pdf')
