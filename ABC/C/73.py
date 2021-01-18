from collections import defaultdict
n = int(input())

A = defaultdict(int)

for i in range(n):
    a = int(input())
    if not A[a]:
        A[a] = True
    else:
        A[a] = False

ans = list(A.values())
print(ans.count(True))