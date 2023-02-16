import numpy as np

left = np.array()

np.save('../left.npy',left)
print(np.load('../left.npy'))

right = np.array()

np.save('../right.npy',right)
print(np.load('../right.npy'))