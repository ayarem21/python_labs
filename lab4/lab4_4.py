input_str = []
temp = {}

for i in range(int(input("Введіть кількість рядків: "))):
    input_str.append(input("Введіть рядок: "))

input_str.sort()

for i in input_str:
    if len(i) in temp.keys():
        temp[len(i)] = temp[len(i)] + f", {i}"
    else:
        temp[len(i)] = i

keys = list(temp.keys())
keys = sorted(keys)

for i in range(len(keys)):
    for j in temp[keys[i]].split(", "):
        print(j)