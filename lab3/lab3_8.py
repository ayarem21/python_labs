stack = [["Говерла", 2061], ["Еверест", 8848], ["Чіліад", 798]]
stack.append(["Гордо", 487])
print(stack)
i = 0
height_count = 0
k = 0
n = 2 #До котрої видаляти
for mountain, height in stack:
    if k < n:
        stack.remove([mountain, height])
    height_count += height
    i += 1
    k += 1
print(i)
print(height_count/i)
print(stack)