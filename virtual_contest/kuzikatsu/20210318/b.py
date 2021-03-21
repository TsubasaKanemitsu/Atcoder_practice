x, y = list(map(int, input().split()))

xx = set({1, 3, 5, 7, 8, 10, 12})
yy = set({4, 6, 9, 11})
zz = set({2})

if set({x}) <= xx and set({y}) <= xx:
    print("Yes")
elif set({x}) <= yy and set({y}) <= yy:
    print("Yes")
else:
    print("No")