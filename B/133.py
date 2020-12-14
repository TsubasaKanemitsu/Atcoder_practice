n, d = list(map(int, input().split()))
count = 0
sm = 0
x = []

for i in range(n):
    x.extend([list(map(int, input().split()))])

for i in range(n):
    for j in range(i + 1, n):
        for k in range(d):
            sm += (x[i][k] - x[j][k]) ** 2
        sm = sm ** 0.5
        if sm.is_integer():
            count += 1
        sm = 0
print(count)
        