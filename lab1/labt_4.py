import math


def f2(x):
    tmp = ((math.cos(x ** 2) ** 2) + x + 2 * math.sin(3 * x)) / -2
    return tmp


def f1(x, a, b, c):
    tmp = 0.5 * x - (((a * x - b) + c) * x - b) / x - 1
    return tmp


x = float(input("Enter x: "))
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
# x = 2
# a = 2
# b = 1
# c = 5
print(f1(x, a, b, c), "\n", f2(x))
