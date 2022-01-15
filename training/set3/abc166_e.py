# 17分
from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

cnt_i = defaultdict(int)
cnt_j = defaultdict(int)

for i in range(n):
    cnt_i[A[i] + i] += 1
    cnt_j[A[i] - i] += 1
ans = 0
for i in range(1, 2 * 10 ** 5):
    ans += cnt_i[i] * cnt_j[-i]
    ans += cnt_i[-i] * cnt_j[i]
print(ans)

# 今回求めたい内容は、
# |i - j| = Ai + Ajを満たす組み合わせの総数を求める

# 愚直解だと、すべてのi - jとAi + Ajの差と和をO(N^2)で計算する必要があるため
# 計算量を落とす必要がある。

# 式変形を行うと
# Ai + Aj - |i - j| = 0
# i < jとすると
# (Ai - i) + (Aj + j) = 0と置き換えることができる
# Ai - iとAj + jはO(N)で求めることができ、
# Ai - iとAj + jが互いの正負が逆で同じ数値になっていればいい