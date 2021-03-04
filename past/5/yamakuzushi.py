n = int(input())

s = [list(input()) for _ in range(n)]

# forの上下限をx, yの上限を超えないようにループを回す
# 関数化しなくてもいいレベル
for i in range(n - 2, -1, -1):
    for j in range(2 * n - 1):
        if s[i][j] == '#':
            if s[i + 1][j - 1] == 'X':
                s[i][j] = 'X'
            if s[i + 1][j] == 'X':
                s[i][j] = 'X'
            if s[i + 1][j + 1] == 'X':
                s[i][j] = 'X'

for i in range(n):
    print(''.join(s[i]))