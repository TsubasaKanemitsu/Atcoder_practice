# 累積和の応用

# 考察
# 現在地から上下左右にどこまで行ったら壁にぶつかるかを調べたい
# 愚直に求めようとすると、O(HW^2)かかる
# 各マスに対して(O(HW)通り)
# 左側に目いっぱい進む(最悪O(W))

# ある特定のマスまでの累積和を求める

h, w = list(map(int, input().split()))
S = [list(input()) for _ in range(h)]

left = [[0] * w for i in range(h)]
right = [[0] * w for i in range(h)]
up = [[0] * w for i in range(h)]
down = [[0] * w for i in range(h)]

for i in range(h):
    cur = 0
    for j in range(w):
        if S[i][j] == '#':
            cur = 0
        else:
            cur += 1
        left[i][j] = cur

for i in range(h):
    cur = 0
    for j in range(w - 1, -1, -1):
        if S[i][j] == '#':
            cur = 0
        else:
            cur += 1
        right[i][j] = cur

for j in range(w):
    cur = 0
    for i in range(h):
        if S[i][j] == '#':
            cur = 0
        else:
            cur += 1
        down[i][j] = cur

for j in range(w):
    cur = 0
    for i in range(h - 1, -1, -1):
        if S[i][j] == '#':
            cur = 0
        else:
            cur += 1
        up[i][j] = cur

ans = 0
for i in range(h):
    for j in range(w):
        temp_ans = left[i][j] + right[i][j] + up[i][j] + down[i][j] - 3
        ans = max(ans, temp_ans)
print(ans)

# グリッドの問題は行と列を分けて考えることもできる
