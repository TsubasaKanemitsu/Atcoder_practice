from collections import deque
import copy

h, w = list(map(int, input().split()))
Q = int(input())

def bfs(gx, gy, sx, sy, flag):
    Q = deque()
    Q.append([sx, sy])
    
    flag2 = copy.deepcopy(flag)
    
    pos = ((1, 0), (0, 1), (-1, 0), (0, -1))

    while len(Q) > 0:
        x, y = Q.popleft()
        if flag2[y][x] != 'r':
            continue
        flag2[y][x] = 'ok'
        for dx, dy in pos:
            X = x + dx
            Y = y + dy
            if 0 <= X < w and 0 <= Y < h:
                if flag2[Y][X] == 'r':
                    Q.append([X, Y])

    if flag2[gy][gx] == 'ok':
        return True
    
    return False

q = []
for i in range(Q):
    qq = list(map(int, input().split()))
    q.append(qq)

flag = [['w'] * w for _ in range(h)]
for i in range(Q):
    if q[i][0] == 1:
        ri, ci = q[i][1] - 1, q[i][2] - 1
        flag[ri][ci] = 'r'
    else:
        ra, ca, rb, cb = q[i][1] - 1, q[i][2] - 1, q[i][3] - 1, q[i][4] - 1
        if bfs(ca, ra, cb, rb, flag):
            print("Yes")
        else:
            print("No")


