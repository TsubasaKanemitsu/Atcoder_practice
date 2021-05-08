import math
n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

_gcd = A[0]
for i in range(1, n):
    _gcd = math.gcd(_gcd, A[i])

if k <= max(A) and _gcd == math.gcd(_gcd, k):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

