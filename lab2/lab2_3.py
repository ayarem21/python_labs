sum = 0
i = 1
while i != 30:
    if i % 2 != 0:
        sum += (i + 10 * i**2) - (i**2 / 7)
        i += 1
    else:
        sum += (i * 2) - i**5
        i += 1
print(sum)