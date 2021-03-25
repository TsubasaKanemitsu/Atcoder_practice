n, m, x = list(map(int, input().split()))

c, a = [], []
for _ in range(n):
    data = list(map(int, input().split()))
    c.append(data[0])
    a.append(data[1:])

ans = 10 ** 100
for bit in range(1 << n):
    point = [0] * m
    money = 0
    flag = True
    for j in range(n):
        if bit & (1 << j):
            for i in range(m):
                point[i] += a[j][i]
            money += c[j]
    for i in range(m):
        if point[i] < x:
            flag = False
            break
    if flag:
        ans = min(ans, money)
    
if ans == 10 ** 100:
    print(-1)
    exit()
print(ans)