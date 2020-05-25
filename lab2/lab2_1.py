i = 0
sum = 0
while i != 100:
    i = int(input("Enter i: "))
    if i % 3 == 0 and i % 5 > 0:
        sum += i
        print(i, " Sum:", sum)
    else:
        print("To exit enter a100, or try again: ")