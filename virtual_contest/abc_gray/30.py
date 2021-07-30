# ABC 163 C
# 10min
# ちょっと詰まった

# 10分
from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

# i = Ai
cnt = defaultdict(int)

for i in range(n - 1):
    cnt[A[i]] += 1

for i in range(1, n + 1):
    print(cnt[i])