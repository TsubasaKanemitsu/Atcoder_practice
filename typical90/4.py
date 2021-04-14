# 8分
# 行毎と列毎の総和を算出し，自分自身を引いた値が各場所における値となる
# 類題: ABC 129 D (Lamo), ARC077 D(包除原理)
h, w = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(h)]

row_sum = []
for i in range(h):
    row_sum.append(sum(A[i]))

col_sum = []
for j in range(w):
    temp_sum = 0
    for i in range(h):
        temp_sum += A[i][j]
    col_sum.append(temp_sum)

ans = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        ans[i][j] = str(row_sum[i] + col_sum[j] - A[i][j])

for i in range(h):
    print(" ".join(ans[i]))