from collections import defaultdict
import heapq
n, m = list(map(int, input().split()))

graph = defaultdict(list)

for _ in range(m):
    a, b, c = list(map(int, input().split()))
    graph[a].append([b, c])


def diijkstra(s, t, k):
    if s == t:
        return 0
    # 各頂点からの距離
    dist = [-1] * (n + 1)

    # ヒープから取り出したことのある頂点か
    done = [False] * (n + 1)

    Q = []
    heapq.heappush(Q, (0, s))

    # 始点の距離
    dist[s] = 0

    while len(Q) > 0:
        d, i = heapq.heappop(Q)
        if done[i]:
            continue

        done[i] = True
        # 頂点iに隣接する頂点を順番に見る
        # 見ている頂点をjとする
        for j, cost in graph[i]:
            if j > k and j != s and j != t:
                continue
            if dist[j] == -1 or dist[j] > dist[i] + cost:
                dist[j] = dist[i] + cost
                heapq.heappush(Q, (dist[j], j))
    if done[t]:
        return dist[t]
    else:
        return 0


ans = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            cost = diijkstra(i + 1, j + 1, k + 1)
            ans += cost
            
print(ans)