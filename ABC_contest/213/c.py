# やり方はわかっていたが、実装に手間取った  
# 座標圧縮
from collections import defaultdict
h, w, n = list(map(int, input().split()))

comb = []
# 行列に存在する値の位置
row = []
col = []

for i in range(n):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    row.append(a)
    col.append(b)
    comb.append((a, b))
    # 行列のリストを作成
    # 座標圧縮する(値が存在する行 or 列を座標とし、値が存在しない個数を累積値として格納する)
row.sort()
col.sort()

comp_row = defaultdict(int)
comp_col = defaultdict(int)
prev_row = -1
prev_col = -1

row_cnt = 0
col_cnt = 0
for i in range(n):
    r = row[i]
    c = col[i]
    if r != prev_row:
        row_cnt += (r - prev_row - 1)
    comp_row[r] = row_cnt
    prev_row = r

    if c != prev_col:
        col_cnt += (c - prev_col - 1)
    comp_col[c] = col_cnt
    prev_col = c
for a, b in comb:
    a_pos = a - comp_row[a] + 1
    b_pos = b - comp_col[b] + 1
    print(a_pos, b_pos)