from collections import defaultdict

N = int(input())
P = list(map(int, input().split()))
Q = int(input())
UD = [list(map(int, input().split())) for _ in range(Q)]

graph = defaultdict(list)

for i, p in enumerate(P):
    # graph[i + 1].append(p)
    graph[p].append(i + 1)

visited = [False] * (N + 1)
number_of_edges = [0] * (N + 1)
is_edges = [0] * (N + 1)

def dfs(v):
    visited[v] = True
    is_edges[v] = 1

    for e in graph[v]:
        if not visited[e]:
            number_of_edges[e] = number_of_edges[v] + 1
            dfs(e)

    is_edges[v] -= 1

dfs(1)

cnt = [0] * (N + 1)

for i in range(len(number_of_edges)):
    num = number_of_edges[i]
    cnt[num] += 1

for i in range(len(UD)):
    u, d = UD[i]
    print(cnt[d])