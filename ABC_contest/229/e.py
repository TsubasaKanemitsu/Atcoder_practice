from collections import defaultdict
n, m = list(map(int, input().split()))

G = defaultdict(list)

for _ in range(m):
    a, b = list(map(int, input().split()))
    G[a].append(b)
    G[b].append(a)

# union find?
