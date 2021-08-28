# ABC 107C
# 15分
# 消したい行と列を算出し、その条件以外の行列で再構築すればいい

h, w = list(map(int, input().split()))
A = [list(input()) for _ in range(h)]

# 行カウント
row = set()
for i in range(h):
    if A[i].count('#') == 0:
        row.add(i)

col = set()
for i in range(w):
    cnt = 0
    for j in range(h):
        if A[j][i] == '#':
            cnt += 1
    if cnt == 0:
        col.add(i)

ans = []

for i in range(h):
    temp = []
    if i in row:
        continue
    for j in range(w):
        if j in col:
            continue
        temp.append(A[i][j])
    ans.append(temp)

for i in range(len(ans)):
    print(''.join(ans[i]))
