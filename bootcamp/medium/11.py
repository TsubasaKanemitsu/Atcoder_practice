# 14分
# 実装に手間取った
n, m = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(n)]
CD = [list(map(int, input().split())) for _ in range(m)]

ans = []
for i in range(n):
    a, b = AB[i]
    dist = 10 ** 99
    check_point = 1
    for j in range(m):
        c, d = CD[j]
        di = abs(a - c) + abs(b - d)
        if di < dist:
            dist = di
            check_point = j + 1
    ans.append(check_point)

for a in ans:
    print(a)