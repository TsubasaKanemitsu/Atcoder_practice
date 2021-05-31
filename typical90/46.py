# 9分
# 倍数になりえるかどうかをmodから判定する

from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

a_cnt = defaultdict(int)
b_cnt = defaultdict(int)
c_cnt = defaultdict(int)

for i in range(n):
    a_cnt[A[i] % 46] += 1
    b_cnt[B[i] % 46] += 1
    c_cnt[C[i] % 46] += 1

ans = 0
for k1, v1 in a_cnt.items():
    for k2, v2 in b_cnt.items():
        for k3, v3 in c_cnt.items():
            if (k1 + k2 + k3) % 46 == 0:
                ans += v1 * v2 * v3
print(ans)