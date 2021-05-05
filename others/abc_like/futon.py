# 下と右だけをみていけばいい
# 重複がなくなる
# 12分 1WA
h, w = list(map(int, input().split()))
s = [list(input()) for _ in range(h)]

cnt = []
for i in range(h):
    for j in range(w):
        pos = ((1, 0), (0, 1))
        for dx, dy in pos:
            x = j + dx
            y = i + dy
            if 0 <= x < w and 0 <= y < h and s[i][j] == '.':
                if s[y][x] == '.':
                    cnt.append([j, x])
print(len(cnt))