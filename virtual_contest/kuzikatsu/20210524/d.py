from collections import Counter
n = int(input())
A = list(map(int, input().split()))

AA = [A[i] - (i + 1) for i in range(n)]

AA.sort()

if n % 2 == 1:
    mid = AA[n // 2]
else:
    mid = (AA[n // 2 - 1] + AA[n // 2]) // 2

ans = 0
for i in range(n):
    ans += abs(AA[i] - mid)
print(ans)