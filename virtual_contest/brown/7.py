# ABC 154D
# 20 min
# 期待値問題

# 考察
# 1. 各サイコロが独立した期待値をもつので、まずは各サイコロの期待値を求める
# 2. 隣接するK個の期待値の最大値を求める必要があるが、sum(Ep[i:i + k])では
# O(N ** 2)になるため、1つサイコロを変えたときの差分をとって、計算量を押さえる
# 3. あとは実装すればO(N)で解ける


# 備考
# 累積和でも解ける

n, k = list(map(int, input().split()))
p = list(map(int, input().split()))

Ep = []

for i in range(n):
    Ep.append((p[i] + 1) / 2)

ans = 0
sm = 0

for i in range(n):
    if i < k:
        sm += Ep[i]
    else:
        ans = max(ans, sm)
        sm = sm + (Ep[i] - Ep[i - k])
ans = max(ans, sm)
print(ans)