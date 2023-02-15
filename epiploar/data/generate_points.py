import numpy as np

left = np.array([[963, 926, 1], [254, 115, 1],
                [859, 621, 1],[496, 568, 1],
                [657, 337, 1],[725, 243, 1],
                [276, 572, 1],[478, 637, 1]])

np.save('../left.npy',left)
print(np.load('../left.npy'))

right = np.array([[831, 918, 1],[218, 91, 1],
                [827, 611, 1],[462, 558, 1],
                [632, 325, 1],[702, 233, 1],
                [225, 554, 1], [428, 624, 1]])

np.save('../right.npy',right)
print(np.load('../right.npy'))