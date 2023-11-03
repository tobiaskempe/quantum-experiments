
import numpy as np
NPQs = np.load(f'marks/pegasus/NPQ.npy').tolist()
print(NPQs)


a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)

np.save('test.npy', a)
b = np.load('test.npy')

print(b)

print(b.tolist())
