# おしかった
# ほぼ正解(全探索の方法が間違えていた)

from collections import deque
h, w = list(map(int, input().split()))

S = [list(input()) for _ in range(h)]

def bfs(sx, sy):
    Q = deque()
    Q.append((sx, sy))
    dist = [[0] * w for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    visited[sy][sx] = True

    while len(Q) > 0:
        x, y = Q.popleft()
        pos = ((0, 1), (0, -1), (1, 0), (- 1, 0))
        for dx, dy in pos:
            X = x + dx
            Y = y + dy
            if not 0 <= X < w or not 0 <= Y < h:
                continue
            if visited[Y][X]:
                continue
            if S[Y][X] == '#':
                continue
            visited[Y][X] = True
            dist[Y][X] += dist[y][x] + 1
            Q.append((X, Y))
    return dist


road = []
for i in range(h):
    for j in range(w):
        if S[i][j] == '.':
            road.append((j, i))
ans = 0
for sx, sy in road:
    dist = bfs(sx, sy)
    for i in range(h):
        ans = max(ans, max(dist[i]))
print(ans)
