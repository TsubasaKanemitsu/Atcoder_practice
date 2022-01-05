# https://drken1215.hatenablog.com/entry/2020/01/26/234000
import math
import bisect

n, d, a = list(map(int, input().split()))

X = []
XH = []
for i in range(n):
    x, h = list(map(int, input().split()))
    XH.append((x, h))
    X.append(x)

X.sort()
# モンスターの位置でソートする
XH.sort(key=lambda x:x[0])

# 貪欲法で左端で爆発させることを愚直にやろうとすると
# どこまでが爆発範囲であるかを探索するのに、O(N^2)かかるので
# 高速化を考える必要がある
# 考察
# 区間[l, r]に爆発したダメージがいくらであったのかを求める必要がある

damage = [0] * (n + 1)
ans = 0
for i in range(n):
    x, h = XH[i]

    if damage[i] < h:
        cnt = math.ceil((h - damage[i]) / a)
    
        # 左端まで爆発させるには、爆弾をx + dで爆発させるので
        # 右端はx + 2 * dとなる
        right = x + 2 * d
        idx = bisect.bisect_right(X, right)
        damage[i] += cnt * a
        damage[idx] -= cnt * a
        ans += cnt

    damage[i + 1] += damage[i]

print(ans)
