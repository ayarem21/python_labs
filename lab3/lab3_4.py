ann, boris = list(map(int, input().split()))
a = set()
b = set()
for i in range(ann):
    a.add(int(input()))
print("")
for i in range(boris):
    b.add(int(input()))

print(len(a.intersection(b)))
print(sorted(a.intersection(b)))
print(len(a.difference(b)))
print(list(reversed(sorted(a.difference(b)))))
print(len(b.difference(a)))
print(list(reversed(sorted(b.difference(a)))))