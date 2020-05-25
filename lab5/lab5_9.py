# Лабораторна робота 5
# Завдання: 9
# Ковтун К. М.
# 06/05/2020

import operator

input_file = open("5_9.txt", 'r')
Students = dict()
Subjects = dict()
for line in input_file:
    if (line == "\n"):
        continue
    if (line.__contains__("ПІБ")):
        subj = line.split()
        for i in range(1, len(subj), 1):
            Subjects[subj[i]] = 0
        continue
    strs = line.split()
    key = strs[0]
    value = [int(i) for i in strs[1:len(strs)]]
    Students[key] = value
input_file.close()
Index_subj = 0
for key1, value1 in Subjects.items():
    Sum_rates = 0
    Count_stud = 0
    for key2, value2 in Students.items():
        Sum_rates += value2[Index_subj]
        Count_stud += 1
    Index_subj += 1
    Subjects[key1] = (Sum_rates / Count_stud)
print("Середній рейтинг предметів:")
for key, value in Subjects.items():
    print(str(key) + " - " + str(value))
Rating = dict()
for key, value in Students.items():
    Sum = 0
    for r in value:
        Sum += r
    Rating[key] = (Sum / len(value))
print()
print("Середній рейтинг групи:")
for key, value in Rating.items():
    print(str(key) + " - " + str(value))
print()
Rating = sorted(Rating.items(), key=operator.itemgetter(1))
Max_rating = Rating[len(Rating)-1]
print("Максимальна оцінка:")
for rating in Rating:
    if (rating[1] == Max_rating[1]):
        print(str(rating))
print()
Min_rating = Rating[0]
print("Мінімальна оцінка:")
for rating in Rating:
    if (rating[1] == Min_rating[1]):
        print(str(rating))


