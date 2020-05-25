result = ""
for i in range(6, 3, -1):
    if (i == 1):
        result = "негритенок"
        result += " пошел"
    else:
        if (i >= 2 and i <= 4):
            result = "негритенка"
        if (i >= 5 and i <= 10):
            result = "негритят"
        result += " пошли"
    print(i, " ", result, " ")
