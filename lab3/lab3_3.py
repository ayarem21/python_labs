import random

count = 0
a = [random.randint(0, 100) for i in range(100)]
print(a, "\n\n")
b = [random.randint(0, 100) for i in range(100)]
print(b)
c = list(set(a) & set(b))
c.sort(reverse = True)
print(' '.join([str(i) for i in c
                if i % 2 == 0]))