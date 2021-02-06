n, x = list(map(int, input().split()))
a = list(map(int, input().split()))

_a = []

for i in a:
    if i != x:
        _a.append(i)

if len(_a) == 0:
    print()
else:
    for i in range(len(_a)):
        print(_a[i], end=' ')