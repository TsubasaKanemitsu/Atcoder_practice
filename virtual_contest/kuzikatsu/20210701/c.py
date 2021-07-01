# ちょっと詰まった
# 固定して考える系
# 連立方程式

C = [list(map(int, input().split())) for _ in range(3)]

flag1 = False
if C[0][0] - C[0][1] == C[1][0] - C[1][1] == C[2][0] - C[2][1]:
    flag1 = True

flag2 = False
if C[0][1] - C[0][2] == C[1][1] - C[1][2] == C[2][1] - C[2][2]:
    flag2 = True

if flag1 and flag2:
    print("Yes")
else:
    print("No")