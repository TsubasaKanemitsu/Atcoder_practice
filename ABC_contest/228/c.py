from collections import defaultdict
n, k = list(map(int, input().split()))
P = [list(map(int, input().split())) for _ in range(n)]

# 自分以外が最低点を取った場合と
# 自分が最高点をとった場合を比較する

point = []

for i in range(n):
    point.append([i, sum(P[i])])

point.sort(key=lambda x:x[1], reverse=True)

ans = defaultdict(bool)

for i in range(n):
    idx, pp = point[i]
    if i > k - 1:
        if pp + 300 >= point[k - 1][1]:
            ans[idx] = True
        else:
            ans[idx] = False
    else:
        ans[idx] = True
ans = sorted(ans.items())
for key, value in ans:
    if value:
        print("Yes")
    else:
        print("No")