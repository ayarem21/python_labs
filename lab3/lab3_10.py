old_dict = {'Studium': "Навчання", 'Pause': "Перерва", 'Lektion': "Урок", 'Lehrer': "Вчитель"}

new_dict = dict([(value, key) for key, value in old_dict.items()])

for i in old_dict:
    print(i, " :  ", old_dict[i])

print()

for i in new_dict:
    print(i, " :  ", new_dict[i]) 