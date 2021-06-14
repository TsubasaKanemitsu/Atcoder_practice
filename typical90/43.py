from collections import deque
import pprint
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
    curve_cnt = [[0] * w for _ in range(h)]
    
    visited[0][0] = True
    
    pre_st = (sx - 1, sy - 1)
    pre_Q = deque()
    pre_Q.append(pre_st)

    while len(Q) > 0:
        pre_x, pre_y = pre_Q.popleft()
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
            
            diff_x = abs(x - pre_x)
            diff_y = abs(y - pre_y)
            if diff_x == 0 and diff_y == 1:
                if abs(pre_x - X) == 1:
                    curve_cnt[Y][X] = curve_cnt[y][x] + 1
                else:
                    curve_cnt[Y][X] = curve_cnt[y][x]
            if diff_x == 1 and diff_y == 0:
                if abs(pre_y - Y) == 1:
                    curve_cnt[Y][X] = curve_cnt[y][x] + 1
                else:
                    curve_cnt[Y][X] = curve_cnt[y][x]
            pre_Q.append((x, y))
    return curve_cnt[gy - 1][gx - 1]


print(bfs())
