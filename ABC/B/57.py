n, m = list(map(int, input().split()))

a = []
b = []
c = []
d = []
for i in range(n):
    _a, _b = list(map(int, input().split()))
    a.append(_a)
    b.append(_b)
for i in range(m):
    _c, _d = list(map(int, input().split()))
    c.append(_c)
    d.append(_d)

dist = 10 ** 36
check_point = []

for i in range(n):
    dist = 10 ** 36
    for j in range(m):
        temp_dist = abs(a[i] - c[j]) + abs(b[i] - d[j])
        if dist > temp_dist:
            dist = temp_dist
            ch_point = j
    check_point.append(ch_point)

for i in check_point:
    print(i + 1)