# 6WA
# 1時間
# 町i => 町i の道を通る場合と
# 町i ~ 町jの道を通って町iに戻ってくる2パターンのうちの最小経路を
# 求めればいい
import heapq
from collections import defaultdict

n, m = list(map(int, input().split()))

graph = defaultdict(list)

for i in range(m):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    graph[a].append([b, c])

def dijkstra(v):
    v -= 1
    Q = []
    heapq.heappush(Q, (0, v))
    
    dist = [0] * n
    self_dist = [10 ** 99] * n
    done = [False] * n
    
    while len(Q) > 0:
        d, i = heapq.heappop(Q)
        if done[i]:
            continue
        
        done[i] = True
        for j, cost in graph[i]:
            if v == i == j:
                self_dist[i] = min(cost, self_dist[i])
            else:
                if dist[j] == 0 or dist[j] > dist[i] + cost:
                    dist[j] = dist[i] + cost
                    heapq.heappush(Q, (dist[j], j))
    
    if dist[v] == 0 and self_dist[v] == 10 ** 99:
        return -1
    else:
        if dist[v] == 0:
            return self_dist[v]
        elif self_dist[v] == 10 ** 99:
            return dist[v]
        else:
            return min(self_dist[v], dist[v])


for i in range(1, n + 1):
    ans = dijkstra(i)
    if ans == 0:
        print(-1)
    else:
        print(ans)