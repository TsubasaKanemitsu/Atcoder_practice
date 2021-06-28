n = int(input())
p = [0] + list(map(int, input().split()))
P = sum(p)
exists = [[False] * (P + 1) for _ in range(n + 1)]

exists[0][0] = True

for i in range(1, n + 1):
    for ps in range(P + 1):
        # 解く場合と解かない場合の2パターンを1度にメモ化する
        # 解かない
        if exists[i - 1][ps]:
            exists[i][ps] = True
        # 解く
        # 前の状態が存在する
        if ps - p[i] >= 0 and exists[i - 1][ps - p[i]]:
            exists[i][ps] = True

ans = 0
for i in range(P + 1):
    if exists[n][i]:
        ans += 1
print(ans)