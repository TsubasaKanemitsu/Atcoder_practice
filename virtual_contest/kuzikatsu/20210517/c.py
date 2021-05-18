import math
n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
A.insert(0, 0)
A.append(n + 1)

width = 10 ** 99
white = []
for i in range(m + 1):
    white.append(A[i + 1] - (A[i] + 1))

width = 10 ** 99
for w in white:
    if w != 0:
        width = min(width, w)

ans = 0
for w in white:
    ans += math.ceil(w / width)
print(ans)