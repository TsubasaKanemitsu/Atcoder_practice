# ABC 206 C
# 15 min
# 解き方 下とほぼ同じ
# https://blog.hamayanhamayan.com/entry/2021/06/19/233714
# 前に出現する値の保存
# jを固定化し、手前に出現しているA[i]のうちA[j]と一致しない数を
# 高速に求めれればいい

# O(N)の解法
from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

ans = 0
cnt = defaultdict(int)
cnt[A[0]] += 1
for i in range(1, n):
    ans += i - cnt[A[i]]
    cnt[A[i]] += 1
print(ans)

# O(NlogN)の解法
# 全組み合わせ - 被る組み合わせ(== 被らない組み合わせ == 余事象を求める)