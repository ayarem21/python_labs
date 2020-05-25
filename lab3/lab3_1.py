import random

count = 0
array = [random.randint(-10, 50) for i in range(10)]
print(array)
for i in range(10):
    if array[i] % 10 == 0:
        print(array[i], "\n", "*")
        count += 1
    else:
        print(array[i])
print("\n", count)