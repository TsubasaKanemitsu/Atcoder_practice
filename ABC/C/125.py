import math
n = int(input())
A = list(map(int, input().split()))

lft = [A[0]]
rgt = [A[-1]]

for i in range(1, n - 1):
    lft.append(math.gcd(lft[i - 1], A[i]))

for i in range(1, n - 1):
    rgt.append(math.gcd(rgt[i - 1], A[n - (i + 1)]))

ans = 0

for i in range(n):
    if i == 0:
        ans = max(ans, rgt[- 1])
    elif i == n - 1:
        ans = max(ans, lft[-1])
    else:
        ans = max(ans, math.gcd(lft[i - 1], rgt[n - (i + 2)]))
print(ans)