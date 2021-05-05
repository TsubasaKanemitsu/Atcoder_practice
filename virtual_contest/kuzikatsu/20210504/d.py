# ABC 112C
# 1時間
# 1WA
# 想定解法と若干違う
# 実装重い系問題

n = int(input())

XYH = [list(map(int, input().split())) for _ in range(n)]

ans = []
for Cx in range(101):
    for Cy in range(101):
        for i in range(n):
            x, y, h = XYH[i]
            H = h + abs(x - Cx) + abs(y - Cy)
            cnt = 0
            for j in range(n):
                xx, yy, hh = XYH[j]
                if hh == max(H - abs(xx - Cx) - abs(yy - Cy), 0):
                    cnt += 1
            if cnt == n:
                ans = [Cx, Cy, H]

for a in ans:
    print(a, end=' ')
print()