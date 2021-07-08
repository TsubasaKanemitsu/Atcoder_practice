# 1WA
# 5分
# 左端と右端の幅を狭めていく問題

n, m = list(map(int, input().split()))
LR = [list(map(int, input().split())) for _ in range(m)]

L = 0
R = n - 1

for i in range(m):
    l, r = LR[i]
    l -= 1
    r -= 1
    L = max(L, l)
    R = min(R, r)

# 注意
if R < L:
    print(0)
else:
    print(R - L + 1)