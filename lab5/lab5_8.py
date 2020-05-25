# Лабораторна робота 5
# Завдання: 8
# Ковтун К. М.
# 01/05/2020

input_file = open("5_8.txt", 'r')
Fruits = dict()
Vitamines = list()
for line in input_file:
    if (line == "\n"):
        continue
    if (line.__contains__("Вид")):
        vit = line.split()
        for i in range(1, len(vit) - 1, 1):
            Vitamines.append(vit[i])
        continue
    strs = line.split()
    key = strs[0]
    value = [float(i) for i in strs[1:len(strs)]]
    Fruits[key] = value
input_file.close()
print("Всі фрукти:")
for key, value in Fruits.items():
    print(str(key) + " - " + str(value))
print("Всі вітаміни: " + str(Vitamines))
search_vitamine = str(input("Введіть вітамін: "))
Index = Vitamines.index(search_vitamine)
Max = 0
fruit = ""
for key, value in Fruits.items():
    if (value[Index] > Max):
        Max = value[Index]
        fruit = key
print("Фрукти: " + str(fruit) + "; max = " + str(Max))
needed_count = float(input("Введіть кількість вітаміну: "))
for key, value in Fruits.items():
    temp_count = value[Index]
    temp_weight = value[len(value)-1]
    needed_weight = (needed_count * temp_weight) / temp_count
    print("Фрукти: " + str(key) + "; потрібна вага = " + str(needed_weight))
arr_fruits = []
while(True):
    Str = str(input("Введіть фрукти: "))
    if (Str == "Кінець"):
        break
    arr_fruits.append(Str)
count_vitamines = [0 for i in range(0, len(Vitamines), 1)]
for key, value in Fruits.items():
    if (arr_fruits.__contains__(key)):
        for i in range(0, len(value) - 1, 1):
            count_vitamines[i] += value[i]
print("Кількість вітамінів: " + str(count_vitamines))

