h, w, x, y = list(map(int, input().split()))

cnt = 0

s = [list(input()) for _ in range(h)]
x -= 1
y -= 1
cnt = 1

for j in range(y - 1, -1, -1):
    if s[x][j] == '.':
        cnt += 1
    else:
        break
for j in range(y + 1, w):
    if s[x][j] == '.':
        cnt += 1
    else:
        break
for i in range(x + 1, h):
    if s[i][y] == '.':
        cnt += 1
    else:
        break
for i in range(x - 1, -1, -1):
    if s[i][y] == '.':
        cnt += 1
    else:
        break
print(cnt)