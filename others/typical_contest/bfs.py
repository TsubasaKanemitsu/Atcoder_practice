from collections import deque
r, c = list(map(int, input().split()))
sy, sx = list(map(int, input().split()))
sy, sx = sy - 1, sx - 1
gy, gx = list(map(int, input().split()))
gy, gx = gy - 1, gx - 1
C = [list(input()) for _ in range(r)]

Q = deque()
Q.append([sx, sy])
visited = [[False] * c for _ in range(r)]

dist = [[0] * c for _ in range(r)]

while len(Q) > 0:
    x, y = Q.popleft()
    pos = ((0, 1), (0, -1), (1, 0), (-1, 0))
    for dx, dy in pos:
        X = x + dx
        Y = y + dy
        if not 0 <= X < c or not 0 <= Y < r:
            continue
        if C[Y][X] == '#':
            continue
        if not visited[Y][X]:
            visited[Y][X] = True
            dist[Y][X] = dist[y][x] + 1
            Q.append([X, Y])

print(dist[gy][gx])