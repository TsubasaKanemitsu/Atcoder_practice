n = int(input())
AB = [list(map(int, input().split())) for _ in range(n)]

ans = 2 * 10 ** 5 + 1

for i in range(n):
    for j in range(n):
        if i != j:
            ans = min(ans, max(AB[i][0], AB[j][1]))
        else:
            ans = min(ans, AB[i][0] + AB[j][1])
print(ans)