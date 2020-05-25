import random

n = int(input("Enter a natural number: "))
rnd = random.uniform(0, 20)
max = rnd
min = rnd
for i in range(0, n):
    if max < rnd and i % 2 == 0:
        max = rnd
    if min > rnd and i % 2 == 0:
        min = rnd
    if i % 2 == 0:
        print(rnd)
    rnd = random.uniform(0, 20)

print("Max: ", max, "\n", "Min: ", min)
print("Sum: ", max + min)