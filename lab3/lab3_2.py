import random

count = 0
a = [random.randint(0, 100) for i in range(100)]
print(a, "\n\n")
b = [random.randint(0, 100) for i in range(100)]
print(b)
for i in a:
    for j in b:
        if i == j and i % i == 0 and j % j == 0 and i > 1 and j > 1:
            count += 1
print(count)