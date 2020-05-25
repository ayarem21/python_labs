import math

sum = 0
a: float = -2
b: float = 2.7
x = a
while x <= b:
    if a <= 1:
        sum += math.sqrt(0.8 - 0.1 * x)
        x += 0.3
        print("Sum <= 1: ", sum)
    if x > 1:
        sum += 5 * math.log(x) + math.cos(x)
        x += 0.3
        print("Sum > 1: ", sum)