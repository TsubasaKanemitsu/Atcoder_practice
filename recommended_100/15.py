# 10分
# 経路がN!通りある
# 順列全探索(Nの制約が2 <= N < 8)
import itertools
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

path = [i for i in range(n)]
length = 0
perm_cnt = 0
for perm in itertools.permutations(path):
    perm_cnt += 1
    for i in range(len(perm) - 1):
        ii = perm[i]
        jj = perm[i + 1]
        length += ((xy[ii][0] - xy[jj][0]) ** 2 + (xy[ii][1] - xy[jj][1]) ** 2) ** 0.5
print(length / perm_cnt)