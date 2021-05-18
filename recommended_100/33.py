# 40分
# 最短経路の座標取得に時間が掛かった

from collections import deque
from collections import defaultdict
h, w = list(map(int, input().split()))
graph = [list(input()) for _ in range(h)]

def bfs():
    st = (0, 0)
    Q = deque()
    Q.append(st)
    
    visited = [[False] * w for _ in range(h)]
    dist = [[0] * w for _ in range(h)]
    route_map = defaultdict(tuple)
    route_map[0] = (0, 0)

    visited[0][0] = True
    while len(Q) > 0:
        x, y = Q.popleft()
        pos = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for dx, dy in pos:
            X = x + dx
            Y = y + dy
            if not 0 <= X < w or not 0 <= Y < h:
                continue
            if graph[Y][X] == '#':
                continue
            if visited[Y][X]:
                continue
            dist[Y][X] = dist[y][x] + 1
            route_map[dist[y][x] + 1] = (X, Y)
            visited[Y][X] = True
            Q.append((X, Y))
    
    return dist, route_map


dist, route_map = bfs()
if dist[h - 1][w - 1] == 0:
    print(-1)
else:
    cnt = 0
    pos = []
    for k, v in route_map.items():
        if k <= dist[-1][-1]:
            pos.append(v)
    for i in range(h):
        for j in range(w):
            if (j, i) not in pos and graph[i][j] == '.':
                cnt += 1
    print(cnt)