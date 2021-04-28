from collections import defaultdict
import itertools

n, m = list(map(int, input().split()))
AB = []

graph = defaultdict(list)

for _ in range(m):
    a, b = list(map(int, input().split()))
    AB.append([a, b])
    graph[a].append(b)
    graph[b].append(a)

if m == 0:
    print(3 ** n)
    exit()

print(graph)

ans = 0
for i in range(1, n + 1):
    if len(graph[i]) >= 3:
        continue
    elif len(graph[i]) == 2:
        ans += len(graph[i])
    elif len(graph[i]) == 1:
        ans += len(graph[i])
print(ans)

