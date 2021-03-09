n, m, x = list(map(int, input().split()))
c = []
a = []

for i in range(n):
    data = list(map(int, input().split()))
    c.append(data[0])
    a.append(data[1:])

ans = 12 * 10 ** 5 + 1
for bit in range(1 << n):
    understand = [0] * m
    money = 0
    flag = True
    for i in range(n):
        if bit & 1 << i:
            for j in range(m):
                understand[j] += a[i][j]
            money += c[i]
    for j in range(m):
        if understand[j] < x:
            flag = False
    if flag:
        ans = min(ans, money)

if ans == 12 * 10 ** 5 + 1:
    print(-1)
else:
    print(ans)