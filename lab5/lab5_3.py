import numpy as np

a = np.array([i for i in range(1, 193, 1) if i%2 and i%3], int)
print("Initial array:")
print(str(a))
a = a.reshape((8, 8))
print("Result matrix 8x8:")
print(str(a))
