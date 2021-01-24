# 15分
n, d = list(map(int, input().split()))

x = [list(map(int, input().split())) for _ in range(n)]

count = 0
for i in range(n):
    for j in range(i + 1, n):
        dis = 0
        for k in range(d):
            dis += abs(x[i][k] - x[j][k]) ** 2
        dis = dis ** 0.5
        if dis.is_integer():
            count += 1
print(count)
