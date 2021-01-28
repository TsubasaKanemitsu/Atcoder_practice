n, d = list(map(int, input().split()))
count = 0
for i in range(n):
    x, y = list(map(int, input().split()))
    diff = (x ** 2 + y ** 2) ** 0.5
    if d >= diff:
        count += 1
print(count)