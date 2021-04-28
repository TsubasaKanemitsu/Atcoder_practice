# 35分
# 方針自体はすぐに経った
# 実装に手間取った
from collections import defaultdict
n = int(input())
base = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
pic = defaultdict(bool)
PIC = []
for _ in range(m):
    x, y = list(map(int, input().split()))
    PIC.append([x, y])
    pic[(x, y)] = True

diff = []
base_x = base[0][0]
base_y = base[0][1]
for i in range(1, n):
    x, y = base[i]
    d_x = base_x - x
    d_y = base_y - y
    diff.append([d_x, d_y])

for i in range(m):
    p_base_x, p_base_y = PIC[i]
    cnt = 0
    temp = []
    for j in range(len(diff)):
        d_x, d_y = diff[j]
        pos_x = p_base_x - d_x
        pos_y = p_base_y - d_y
        temp.append([pos_x, pos_y])
        if 0 <= pos_x <= 10 ** 6 and 0 <= pos_x <= 10 ** 6:
            if pic[(pos_x, pos_y)]:
                cnt += 1
    if cnt == len(diff):
        x = p_base_x - base_x
        y = p_base_y - base_y
        print(x, y)
        exit()