import bisect
n, q = list(map(int, input().split()))
A = list(map(int, input().split()))
X = [int(input()) for _ in range(q)]

A.sort()
for x in X:
    idx = bisect.bisect_left(A, x)
    print(n - idx)
