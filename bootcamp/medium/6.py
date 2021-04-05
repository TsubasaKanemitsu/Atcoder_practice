# 11分
H, W = list(map(int, input().split()))

S = [list(input()) for _ in range(H)]


def check_inside(x, y):
    if 0 <= x < W and 0 <= y < H:
        return True
    return False


pos = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
for y in range(H):
    for x in range(W):
        cnt = 0
        if S[y][x] == '.':
            for dx, dy in pos:
                X = x + dx
                Y = y + dy
                if check_inside(X, Y):
                    if S[Y][X] == '#':
                        cnt += 1
            S[y][x] = str(cnt)
for i in range(H):
    print(''.join(S[i]))