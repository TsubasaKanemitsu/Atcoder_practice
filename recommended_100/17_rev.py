# 斜め判定の方法
# クイーンを配置できる場所の性質
# 順列と添え字を用いてx, y座標を出す

import itertools

k = int(input())
num = [i for i in range(8)]

rc = [list(map(int, input().split())) for _ in range(k)]

# p = []
# for perm in itertools.permutations(range(8), 8):
#     cnt = 0
#     for r, c in rc:
#         if perm[r] == c:
#             cnt += 1
#     if cnt == k:
#         p = perm
#         break
# print(p)

# ans = [['.'] * 8 for _ in range(8)]

# for i in range(len(perm)):
#     ans[i][perm[i]] = 'Q'

# for i in range(len(ans)):
#     print(''.join(ans[i]))