# CODEFESTIAL 2017 qual A
n, m, k = list(map(int, input().split()))

# 制約
# 最初は全てのマスが白い
# ボタンを押すとその行、列のマスの色が反転する

# n, m倍は可能
# 交点の数だけ白になる

# (n - btn_row) * btn_col
# (m - btn_col) * btn_row
# これの総和がkになるかどうか?

# if n == 1 and m == 1:
#     print("Yes")
#     exit()

for btn_row in range(n + 1):
    for btn_col in range(m + 1):
        ans = (n - btn_row) * btn_col + (m - btn_col) * btn_row
        if ans == k:
            print("Yes")
            exit()
print("No")