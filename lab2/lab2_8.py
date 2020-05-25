import math

sum = 0
e = 10**(-5)
n = 1
i = 1
while n > e:
    n = 1 / (i**2)
    if i % 2 == 1:
        sum += n
        #n += 1
        print("i % 2 == 1 ", sum)
    if i % 2 == 0:
        sum -= n
        #n += 1
        print("i % 2 == 0 ", sum)
    i += 1
k = sum - (math.pi**2 / 12)
print(k)