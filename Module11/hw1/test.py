import numpy as np

a = np.array(
    [np.arange(1, 101, 10), np.arange(2, 101, 10), np.arange(3, 101, 10), np.arange(4, 101, 10), np.arange(5, 101, 10)])


x = np.hsplit(a, 2)
print(x[0]+x[1])