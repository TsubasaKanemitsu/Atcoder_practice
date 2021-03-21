
h, n = list(map(int, input().split()))

AB = [list(map(int, input().split())) for _ in range(n)]

hp = [10 ** 50] * (h + 10 ** 4)
hp[0] = 0

for i in range(n):
    for j in range(h + 1):
        hp[j + AB[i][0]] = min(hp[j + AB[i][0]], hp[j] + AB[i][1])

ans = min(hp[h:])
print(ans)
