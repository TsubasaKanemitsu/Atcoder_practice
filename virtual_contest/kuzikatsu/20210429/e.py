from collections import defaultdict, deque

n, m = list(map(int, input().split()))
ABC = [list(map(int, input().split())) for _ in range(m)]

graph = defaultdict(list)


for i in range(m):
    a, b, c = ABC[i]
    graph[a].append([b, c])

def bfs(i):
    Q = deque()
    for town, cost in graph[i]:
        Q.append([town, cost])
    dist = [0] * (n + 1)
    
    while len(Q) > 0:
        town, cost = Q.popleft()
        if dist[town] == 0 or dist[town] > dist[i] + cost:
            dist[town] = dist[i] + cost
            Q.extend(graph[town])
        print(Q, dist)
        # if town == i:
        #     return dist[i]
    print(dist)
for i in range(1, n + 1):
    bfs(i)
    