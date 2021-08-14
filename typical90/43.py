from collections import deque
h, w = list(map(int, input().split()))
rs, cs = list(map(int, input().split()))
rt, ct = list(map(int, input().split()))

rs, cs = rs - 1, cs - 1
rt, ct = rt - 1, ct - 1

graph = [list(input()) for _ in range(h)]


def bfs(rs, cs, rt, ct):
    Q = deque()

    dist = [[10 ** 18 + 1] * w for _ in range(h)]
    # 初期化
    for i in range(4):
        dist[rs][cs] = 0
        Q.append((rs, cs, i, 0))

    # 上下左右への移動
    pos = ((-1, 0), (0, -1), (1, 0), (0, 1))
    while len(Q) > 0:
        # print("Q", Q)
        rv, cv, _dir, cost = Q.popleft()
        
        for i in range(4):
            dx = pos[i][0]
            dy = pos[i][1]
            nx = rv + dx
            ny = cv + dy
            
            if not 0 <= nx < h or not 0 <= ny < w:
                continue
            if graph[nx][ny] == '#':
                continue
            
            if _dir != i and dist[nx][ny] > cost:
                dist[nx][ny] = cost + 1
                Q.append((nx, ny, i, cost + 1))
            elif _dir == i and dist[nx][ny] >= cost:
                dist[nx][ny] = cost
                Q.appendleft((nx, ny, i, cost))
    return dist[rt][ct]


dist = bfs(rs, cs, rt, ct)
print(dist)
