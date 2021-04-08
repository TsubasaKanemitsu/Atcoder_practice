h, w = list(map(int, input().split()))
a = [list(input()) for _ in range(h)]

rm = []
# 行チェック
for i in range(h):
    white = a[i].count('.')
    if white == w:
        pos = [(i, j) for j in range(w)]
        rm.extend(pos)
    black = 0
    white = 0

# 列チェック
for j in range(w):
    white = 0
    for i in range(h):
        if a[i][j] == '.':
            white += 1
    if white == h:
        pos = [(i, j) for i in range(h)]
        rm.extend(pos)

ans = []
for i in range(h):
    temp = []
    for j in range(w):
        if (i, j) in rm:
            continue
        temp.append(a[i][j])
    if not temp == []:
        ans.append(temp)
for i in range(len(ans)):
    print(''.join(ans[i]))