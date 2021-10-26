from collections import defaultdict
m = int(input())

graph = defaultdict(list)
puzzle = defaultdict(int)

for i in range(m):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

P = list(map(int, input().split()))

for i in range(9):
    puzzle[i + 1] = 0

for idx, p in enumerate(P):
    puzzle[p] = idx + 1

print(graph, puzzle)