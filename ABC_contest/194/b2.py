n = int(input())

AB = [list(map(int, input().split())) for _ in range(n)]

ans = 12 * 10 ** 5 + 1
for i in range(n):
    for j in range(n):
        ans = min(ans, AB[i][0] + AB[j][1] if i == j else max(AB[i][0], AB[j][1]))
print(ans)