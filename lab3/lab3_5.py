n = int(input())
n = 3 * n + 1
print(n)
ans = set(range(1, n + 1))
q = 0
while True:
    q = input()
    if q == "HELP":
        break
    else:
        a = set(list(map(int, q.split())))
        q = input()
        if q == "YES":
            ans = ans & a
        else:
            ans = ans - a
ans = sorted(ans)
for i in range(0, len(ans)):
    if ans[i] % 3 == 0:
        print(ans[i])