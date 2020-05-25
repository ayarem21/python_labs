str = "Мугам — один из основных жанров азербайджанской традиционной музыки, многочастное вокально-инструментальное произведение, являющееся классическим музыкально-поэтическим искусством азербайджанского народа. Мугам — это также общее название ладов азербайджанской музыки."
str = str.replace("!", ".")
str = str.replace("?", ".")
print(str)
print('Speech count:  ', str.count('.'))
array = []
array = str.split(". ")
for i in range(0, len(array)):
    print('Words count in speech ', i+1, ": ", len(array[i].split()))