c = [list(map(int, input().split())) for _ in range(3)]

flag = True
if c[0][0] - c[0][1] != c[1][0] - c[1][1] or c[0][0] - c[0][1] != c[2][0] - c[2][1]:
    flag = False
if c[0][1] - c[0][2] != c[1][1] - c[1][2] or c[0][1] - c[0][2] != c[2][1] - c[2][2]:
    flag = False
if c[0][0] - c[1][0] != c[0][1] - c[1][1] or c[0][0] - c[1][0] != c[0][2] - c[1][2]:
    flag = False
if c[1][0] - c[2][0] != c[1][1] - c[2][1] or c[1][0] - c[2][0] != c[1][2] - c[2][2]:
    flag = False

if flag:
    print("Yes")
else:
    print("No")