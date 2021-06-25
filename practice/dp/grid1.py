h, w = list(map(int, input().split()))

graph = [list(input()) for _ in range(h)]

pattern = [[0] * w for _ in range(h)]
pattern[0][0] = 1
for y in range(h):
    for x in range(w):
        X1 = x - 1
        Y1 = y
        X2 = x
        Y2 = y - 1
        if 0 <= X1 < w and 0 <= Y1 < h:
            if graph[Y1][X1] == '.' and graph[y][x] == '.':
                pattern[y][x] += pattern[Y1][X1]
        if 0 <= X2 < w and 0 <= Y2 < h:
            if graph[Y2][X2] == '.' and graph[y][x] == '.':
                pattern[y][x] += pattern[Y2][X2]

ans = pattern[h - 1][w - 1]
print(ans % (10 ** 9 + 7))
