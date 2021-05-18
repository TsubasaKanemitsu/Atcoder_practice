from collections import deque
h, w = list(map(int, input().split()))
sy, sx = list(map(int, input().split()))
gy, gx = list(map(int, input().split()))

graph = [list(input()) for _ in range(h)]

def bfs():
    st = (sx - 1, sy - 1)
    Q = deque()
    Q.append(st)
    
    visited = [[False] * w for _ in range(h)]
    dist = [[0] * w for _ in range(h)]
    
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
            visited[Y][X] = True
            Q.append((X, Y))
    
    return dist[gy - 1][gx - 1]

print(bfs())