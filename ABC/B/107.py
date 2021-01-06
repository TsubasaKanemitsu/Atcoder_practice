h, w = list(map(int, input().split()))

A = []

for i in range(h):
    A.extend([list(input())])

remove_row = []
remove_col = []
count_col = [0 for j in range(w)]

# 「.」が全て含まれている行列の位置を探索
for i in range(h):
    row = list(set(A[i]))
    if row[0] == '.' and len(row) == 1:
        remove_row.append(i)
    for j in range(w):
        if A[i][j] == '.':
            count_col[j] += 1

# 削除する列のindex取得
remove_col = [col for col, val in enumerate(count_col) if val == h]

new_A = []
for i in range(h):
    temp_A = []
    for j in range(w):
        if i not in remove_row and j not in remove_col:
            temp_A.extend(A[i][j])
    if not temp_A == []:
        new_A.extend([temp_A])

for a in new_A:
    print(''.join(a))