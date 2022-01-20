# 10分
from collections import deque
h, w = list(map(int, input().split()))

C = [list(input()) for _ in range(h)]


def bfs():
    Q = deque()
    Q.append((0, 0))

    visited = [[False] * w for _ in range(h)]
    dist = [[0] * w for _ in range(h)]

    visited[0][0] = True
    dist[0][0] = 1

    while len(Q) > 0:
        x, y = Q.popleft()

        for dx, dy in ((0, 1), (1, 0)):
            X = x + dx
            Y = y + dy
            if not (0 <= X < h and 0 <= Y < w):
                continue

            if visited[X][Y] or C[X][Y] == '#':
                continue

            dist[X][Y] = dist[x][y] + 1
            visited[X][Y] = True
            Q.append((X, Y))

    max_dist = max([max(d) for d in dist])
    return max_dist

max_dist = bfs()
print(max_dist)