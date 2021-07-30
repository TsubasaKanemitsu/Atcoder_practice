h, w, c = list(map(int, input().split()))

A = [list(map(int, input().split())) for _ in range(h)]

num = []
for i in range(h):
    for j in range(w):
        num.append((A[i][j], i, j))
num.sort(key=lambda x:(x[0], x[1], x[2]))
print(num)

ans = 10 ** 99
for k in range(len(num) - 1):
    aij, i, j = num[k]
    aij_dash, i_dash, j_dash = num[k + 1]
    temp_ans = aij + aij_dash + c * (abs(i - i_dash) + abs(j - j_dash))
    ans = min(ans, temp_ans)
print(ans)