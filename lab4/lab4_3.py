from random import randint

science = []
science.append("Інтерполяція")
science.append("Програмування")
science.append("Строки")
science.append("Класи")
science.append("Об'єкти")
science.append("Поліморфізм")
science.append("Вичислення")
science.append("Формула")
text = input("Введіть текст: ")
text = text + ": _"
rand_index = randint(0, len(science))
text = text.replace("_", science[rand_index])
print(text)

