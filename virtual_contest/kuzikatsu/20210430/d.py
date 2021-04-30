h, w = list(map(int, input().split()))
S = [list(input()) for _ in range(h)]


square = 0
for i in range(h - 1):
    for j in range(w - 1):
        cnt = 0
        pos = ((0, 1), (1, 0), (1, 1), (0, 0))
        for dx, dy in pos:
            x = j + dx
            y = i + dy
            if S[y][x] == '#':
                cnt += 1
        if cnt == 1 or cnt == 3:
            square += 1
print(square)