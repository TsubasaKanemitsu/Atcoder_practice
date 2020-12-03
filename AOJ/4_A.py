a, b = list(map(int, input().split()))

d = int(a / b)
r = int(a % b)
f = round(a / b, 6)

print(d, r, f)

