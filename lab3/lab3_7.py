n = int(input("Введіть кількість слів: "))
List = []
for i in range(1, n+1):
    word = str(input("Введіть слово: "))
    List.append(word)
index = int(input("Введіть індекс слова у: "))
y = List[index-1]
print("Список[", index, "] = ", y)
LenSum = 0
for word in List:
    if (word != y):
        LenSum += 2 * len(word)
    else:
        LenSum += len(word)
print("Сума довжини = ", LenSum)
K = 3
print("Константа K = ", K)
iterator = 0
flag = False
for i in range(1, int(LenSum*K), 1):
    word = List[iterator]
    if (y.find(word) != -1 and int(iterator) != index - 1):
        print(word)
        flag = True
    iterator += 1
    if (iterator == len(List)):
        break
if (flag == True):
    print("Вітаю!")
else:
    print("Вибачте...")