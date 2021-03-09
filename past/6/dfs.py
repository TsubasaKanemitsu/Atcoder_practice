import sys
sys.setrecursionlimit(1000000)

h, w = list(map(int, input().split()))

c = [input() for _ in range(h)]

for i in range(h):
    for j in range(w):
        if c[i][j] == 's':
            sy, sx = i, j
        elif c[i][j] == 'g':
            gy, gx = i, j

visited = [[False] * w for _ in range(h)]

# dfs
def dfs(i, j):
    visited[i][j] = True

    # 4方向探索
    for i2, j2 in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
        if not (0 <= j2 < w and 0 <= i2 < h):
            continue
        if c[i2][j2] == '#':
            continue
        if not visited[i2][j2]:
            dfs(i2, j2)


dfs(sy, sx)

if visited[gy][gx]:
    print("Yes")
else:
    print("No")