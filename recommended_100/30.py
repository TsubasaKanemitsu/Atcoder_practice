# 35分
from collections import defaultdict, deque
h, w, n = list(map(int, input().split()))
route = [list(input()) for _ in range(h)]

point = defaultdict(tuple)
for i in range(h):
    for j in range(w):
        if route[i][j] == 'S':
            st = (j, i)
        elif route[i][j] != 'X' or route[i][j] != '.':
            point[route[i][j]] = (j, i)
point[str(0)] = st


def bfs(st, end):
    Q = deque()
    Q.append(st)
    
    gx, gy = end
    visited = [[False] * w for _ in range(h)]
    dist = [[0] * w for _ in range(h)]
    pos = ((0, 1), (0, -1), (1, 0), (-1, 0))
    while len(Q) > 0:
        x, y = Q.popleft()
        for dx, dy in pos:
            X = x + dx
            Y = y + dy
            if not 0 <= X < w or not 0 <= Y < h:
                continue
            if route[Y][X] == 'X':
                continue
            if visited[Y][X]:
                continue
            visited[Y][X] = True
            dist[Y][X] = dist[y][x] + 1
            if X == gx and Y == gy:
                break
            Q.append((X, Y))
    return dist[gy][gx]


ans = 0
for i in range(1, n + 1):
    st = point[str(i - 1)]
    end = point[str(i)]
    ans += bfs(st, end)
print(ans)
