from collections import defaultdict
n, m = list(map(int, input().split()))

path = defaultdict(int)

for i in range(m):
    a, b = list(map(int, input().split()))
    path[b] += 1
    path[a] += 1

for i in range(1, n + 1):
    print(path[i])
