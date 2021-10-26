n, m = list(map(int, input().split()))
A = [list(input()) for _ in range(2 * n)]

# 人の番号、勝数
info = [[i, 0] for i in range(2 * n + 1)]
for j in range(m):
    for i in range(1, n + 1):
        p1 = info[2 * i - 1][0] - 1
        p2 = info[2 * i][0] - 1
        if (A[p1][j] == 'G' and A[p2][j] == 'C') or (A[p1][j] == 'P' and A[p2][j] == 'G') or (A[p1][j] == 'C' and A[p2][j] == 'P'):
            info[2 * i - 1][1] += 1
        elif (A[p2][j] == 'G' and A[p1][j] == 'C') or (A[p2][j] == 'P' and A[p1][j] == 'G') or (A[p2][j] == 'C' and A[p1][j] == 'P'):
            info[2 * i][1] += 1
        else:
            pass
    info.sort(key=lambda x: (x[1]), reverse=True)
    new_info = []

    for i in range(len(info)):
        if info[i][0] != 0:
            new_info.append(info[i])
    new_info.insert(0, [0, 0])
    info = new_info
    for i in range(1, len(info)):
        for j in range(1, len(info)):
            if i == j:
                continue
            if info[i][1] == info[j][1] and info[i][0] < info[j][0]:
                temp = info[j][0]
                info[j][0] = info[i][0]
                info[i][0] = temp
    
    
ans = []
for i, val in enumerate(info):
    ans.append((i, val[0]))

for a in ans[1:]:
    print(a[1])