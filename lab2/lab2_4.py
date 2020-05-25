n = int(input("Enter a number: "))
sum = 0
x = 1
while x != n:
    if x % 2 == 0:
        sum += x**(2 * x)
        x += 1
    elif x % 2 == 1:
        sum += 3 * x
        x += 1
    else:
        sum += x
        x += 1
print(sum)