import heapq
from collections import defaultdict
n, m = list(map(int, input().split()))

graph = defaultdict(list)

for i in range(m):
    u, v, c = list(map(int, input().split()))
    graph[u].append([v, c])
    
# 各頂点からの距離
dist = [-1] * n

# ヒープから取り出したことのある頂点か
done = [False] * n

Q = []
heapq.heappush(Q, (0, 0))

# 始点の距離
dist[0] = 0

while len(Q) > 0:
    d, i = heapq.heappop(Q)

    if done[i]:
        continue

    done[i] = True

    # 頂点iに隣接する頂点を順番に見る
    # 見ている頂点をjとする
    for j, cost in graph[i]:
        if dist[j] == -1 or dist[j] > dist[i] + cost:
            dist[j] = dist[i] + cost
            heapq.heappush(Q, (dist[j], j))

ans = dist[n - 1]
print(ans)