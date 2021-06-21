A = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]

result = [[False] * 3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        for k in range(n):
            if A[i][j] == b[k]:
                result[i][j] = True

# 行, 列のビンゴ
for i in range(3):
    if result[i].count(True) == 3:
        print("Yes")
        exit()
    if result[0][i] == result[1][i] == result[2][i] == True:
        print("Yes")
        exit()

if result[0][0] == result[1][1] == result[2][2] == True:
    print("Yes")
    exit()
elif result[0][2] == result[1][1] == result[2][0] == True:
    print("Yes")
    exit()
print("No")