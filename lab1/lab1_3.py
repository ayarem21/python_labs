def credit_sum(credit, n, percent):
    sum2 = 0
    for i in range(n):
        sum = credit * (1 + (percent + i) / 100) ** (i + 1)
        sum2 += sum - credit
    return sum2


credit = float(input("Enter credit: "))
n = int(input("Enter year: "))
percent = float(input("Enter percent: "))
sum2 = 0

print("Sum: ", credit_sum(credit, n, percent) + credit)
