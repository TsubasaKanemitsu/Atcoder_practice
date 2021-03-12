from collections import Counter
n, L = list(map(int, input().split()))
X = list(map(int, input().split()))

t1, t2, t3 = list(map(int, input().split()))

# ハードルのある座標においてTrueになる配列
H = [False] * (L + 1)
for x in X:
    H[x] = True


# cost[i]: 座標iで行動を終了するまでの最小所要時間
# 非常に大きな値で初期化しておき，minを用いて更新する
cost = [10 ** 100] * (L + 1)

cost[0] = 0
# 同じ箇所を通ることがあるので，全行動パターンでその地点を通る最小コストを求める

for i in range(1, L + 1):
    # 行動1
    cost[i] = min(cost[i], cost[i - 1] + t1)

    # 行動2
    if i >= 2:
        cost[i] = min(cost[i], cost[i - 2] + t1 + t2)

    if i >= 4:
        cost[i] = min(cost[i], cost[i - 4] + t1 + 3 * t2)

    if H[i]:
        cost[i] += t3

ans = cost[L]
for i in [L - 3, L - 2, L - 1]:
    if i >= 0:
        ans = min(ans, cost[i] + t1 // 2 + t2 * (2 * (L - i) - 1) // 2)
print(ans)