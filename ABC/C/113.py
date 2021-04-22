# 50分
# 2WA
from collections import defaultdict
n, m = list(map(int, input().split()))

city = defaultdict(list)

for i in range(m):
    p, y = list(map(int, input().split()))
    city[p].append([i + 1, y])

new_city = defaultdict(list)
for i in range(n):
    city[i + 1] = sorted(city[i + 1], key=lambda x:x[1])
    CT = city[i + 1]
    for j in range(len(CT)):
        # 市，県，順番
        new_city[i + 1].append([city[i + 1][j][0], i + 1, j + 1])

ans_list = []

for k, v in new_city.items():
    ans_list.extend(v)

ans_list.sort(key=lambda x:x[0])

for c, p, order in ans_list:
    print(str(p).zfill(6) + str(order).zfill(6))