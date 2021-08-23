# ABC 202 C
# 5 min
# 

from collections import Counter
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
BC = []
for i in range(n):
    BC.append(B[C[i] - 1])

a_cnt = Counter(A)
bc_cnt = Counter(BC)

ans = 0
for i in range(1, n + 1):
    ans += a_cnt[i] * bc_cnt[i]
print(ans)