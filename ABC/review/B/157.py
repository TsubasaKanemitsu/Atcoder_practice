a = [list(map(int, input().split())) for _ in range(3)]

n = int(input())

b = [int(input()) for _ in range(n)]

judge = [[False, False, False] for _ in range(3)]
for i in range(3):
    for j in range(3):
        for k in range(n):
            if a[i][j] == b[k]:
                judge[i][j] = True

for i in range(3):
    if judge[i].count(True) == 3:
        print("Yes")
        exit()

for i in range(3):
    if judge[0][i] == judge[1][i] == judge[2][i] == True:
        print("Yes")
        exit()

if judge[0][0] == judge[1][1] == judge[2][2] == True:
    print("Yes")
    exit()
if judge[0][2] == judge[1][1] == judge[2][0] == True:
    print("Yes")
    exit()
print("No")
