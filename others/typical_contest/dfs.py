import sys
sys.setrecursionlimit(10 ** 6)

h, w = list(map(int, input().split()))

graph = [list(input()) for _ in range(h)]

visited = [[False] * w for _ in range(h)]

s = []
g = []

for i in range(h):
    for j in range(w):
        if graph[i][j] == 's':
            s = [j, i]
        elif graph[i][j] == 'g':
            g = [j, i]


def dfs(v):
    x, y = v
    visited[y][x] = True
    pos = ((0, 1), (0, -1), (1, 0), (-1, 0))
    for dx, dy in pos:
        X = x + dx
        Y = y + dy
        if not 0 <= X < w or not 0 <= Y < h:
            continue
        if visited[Y][X]:
            continue
        if graph[Y][X] == '#':
            continue
        dfs([X, Y])
        

dfs(s)

if visited[g[1]][g[0]]:
    print("Yes")
else:
    print("No")
