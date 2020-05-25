import numpy as np
from random import randint

n = int(input("Enter the count of elements in array n: "))
a = np.array([randint(0, 100) for i in range(0, n, 1)], int)
b = np.array([randint(0, 100) for i in range(0, n, 1)], int)
print(a)
print(b)
c = a * b
print(c)

