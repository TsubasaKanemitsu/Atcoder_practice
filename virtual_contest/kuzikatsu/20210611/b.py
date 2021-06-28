h, w, x, y = list(map(int, input().split()))

x -= 1
y -= 1
s = [list(input()) for _ in range(h)]

cnt = 0

for j in range(y, w):
    if s[x][j] == '#':
        break
    else:
        cnt += 1
for j in range(y, -1, -1):
    if s[x][j] == '#':
        break
    else:
        cnt += 1

for i in range(x, h):
    if s[i][y] == '#':
        break
    else:
        cnt += 1

for i in range(x, -1, -1):
    if s[i][y] == '#':
        break
    else:
        cnt += 1

print(cnt - 3)
