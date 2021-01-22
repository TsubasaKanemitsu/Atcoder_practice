from collections import defaultdict
n = int(input())
d, x = list(map(int, input().split()))

A = [int(input()) for _ in range(n)]


chocho = 0
for i in range(n):
    j = 0
    while j * A[i] + 1 <= d:
        day = j * A[i] + 1
        j += 1
    chocho += j

ans = chocho + x
print(ans)