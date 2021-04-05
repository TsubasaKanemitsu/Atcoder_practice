# 1時間
from collections import deque
H, W = list(map(int, input().split()))
S = [list(input()) for _ in range(H)]


move_cnt = [[0] * W for _ in range(H)]
check = [[True] * W for _ in range(H)]

def check_infield(x, y):
    if 0 <= x < W and 0 <= y < H:
        return True
    return False


queue = deque()

start = []
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            start.append([j, i])

pos = ((1, 0), (-1, 0), (0, 1), (0, -1))
ans = 0
for st in start:
    move_cnt = [[0] * W for _ in range(H)]
    check = [[True] * W for _ in range(H)]
    check[st[1]][st[0]] = False
    queue.append(st)
    while len(queue) > 0:
        x, y = queue.popleft()
        for dx, dy in pos:
            X = x + dx
            Y = y + dy
            if check_infield(X, Y) and check[Y][X]:
                if S[Y][X] == '.':
                    check[Y][X] = False
                    queue.append([X, Y])
                    move_cnt[Y][X] = move_cnt[y][x] + 1
    for i in range(H):
        ans = max(ans, max(move_cnt[i]))
print(ans)