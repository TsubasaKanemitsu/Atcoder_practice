n, x = list(map(int, input().split()))
l = list(map(int, input().split()))

d = [0]
count = 0
for i in range(1, n + 1):
    d.append(d[i - 1] + l[i - 1])

for h in d:
    if h <= x:
        count += 1

print(count)