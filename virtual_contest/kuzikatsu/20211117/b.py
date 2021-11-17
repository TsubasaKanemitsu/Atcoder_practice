h, w, x, y = list(map(int, input().split()))

S = [list(input()) for _ in range(h)]

x -= 1
y -= 1

ans = 1
# row
for i in range(x + 1, h):
    if S[i][y] == '#':
        break
    ans += 1
for i in range(x - 1, -1, -1):
    if S[i][y] == '#':
        break
    ans += 1

# col
for j in range(y + 1, w):
    if S[x][j] == '#':
        break
    ans += 1
for j in range(y - 1, -1, -1):
    if S[x][j] == '#':
        break
    ans += 1

print(ans)