from collections import defaultdict
n = int(input())
A = [int(input()) for _ in range(n)]

B = list(set(A))
B.sort()

tr = defaultdict(int)
for idx, b in enumerate(B):
    tr[b] = idx

for a in A:
    print(tr[a])
