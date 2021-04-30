# 6WA
# 1時間
# パターン1: 町i => 町i の道を通る場合と
# パターン2: 町i ~ 町jの道を通って町iに戻ってくる2パターンのうちの最小経路を
# 求めればいい
# 復習する
import heapq
from collections import defaultdict

n, m = list(map(int, input().split()))

graph = defaultdict(list)

# パターン1
for i in range(m):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    graph[a].append([b, c])

self_loop = [10 ** 9] * n

for i in range(n):
    flag = True
    for v, cost in graph[i]:
        if i == v:
            flag = False
            self_loop[i] = min(cost, self_loop[i])
    if flag:
        self_loop[i] = -1

# パターン2
def dijkstra(v):
    v -= 1
    Q = []
    heapq.heappush(Q, (0, v))
    
    dist = [0] * n
    done = [False] * n
    
    while len(Q) > 0:
        d, i = heapq.heappop(Q)
        
        if done[i]:
            continue
        
        done[i] = True
        for j, cost in graph[i]:
            # 自分自身へは行かないようにする
            if i == j:
                continue
            if dist[j] == 0 or dist[j] > dist[i] + cost:
                dist[j] = dist[i] + cost
                heapq.heappush(Q, (dist[j], j))
    if dist[v] == 0:
        return -1
    else:
        return dist[v]


for i in range(1, n + 1):
    if self_loop[i - 1] < 0 and dijkstra(i) < 0:
        print(-1)
    elif self_loop[i - 1] < 0:
        print(dijkstra(i))
    elif dijkstra(i) < 0:
        print(self_loop[i - 1])
    else:
        print(min(self_loop[i - 1], dijkstra(i)))