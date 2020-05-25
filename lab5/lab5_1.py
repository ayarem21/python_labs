import numpy as np

input_file = open('5_1.txt', 'r')
List = []
for line in input_file:
    if (line == "\n"):
        continue
    str_arr = line.split()
    for j in range(0, len(str_arr), 1):
        List.append(str_arr[j])
input_file.close()
print("Count of words: " + str(len(List)))
Str_array = np.array([word for word in List], str)
Str_array = sorted(Str_array, key=lambda x: len(x), reverse=False)
Min_word = Str_array[0]
Max_word = Str_array[len(Str_array)-1]
print("Word with min len (", len(Min_word), "): ", Min_word)
print("Word with max len (", len(Max_word), "): ", Max_word)
output_file = open('5_1_result.txt', 'w')
output_file.write("List of words: " + str(List) + "\n")
a = np.array([len(word) for word in List], int)
output_file.write("Initial array: " + str(a) + "\n")
a.sort()
output_file.write("Sorted array: " + str(a) + "\n")
a = np.sqrt(a)
output_file.write("array: " + str(a) + "\n")
Sum = a.sum()
print("Max - count = ", len(Max_word) - len(a))
output_file.close()
