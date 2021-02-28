a = int(input())
b = int(input())

v = set([a, b])

vv = set([1, 2, 3])

ans = vv - v
print(list(ans)[0])