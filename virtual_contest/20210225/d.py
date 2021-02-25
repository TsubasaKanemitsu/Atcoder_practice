from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))
a = [[i + 1, A[i]] for i in range(n)]

L = defaultdict(int)
R = defaultdict(int)

for i in range(n):
    R[a[i][0] + a[i][1]] += 1
    L[a[i][0] - a[i][1]] += 1

ans = 0
for k, v in R.items():
    ans += R[k] * L[k]
print(ans)