# 6分
# 1WA
# 同じ長さかつ一番長い棒が4本ある場合，正方形にすることもできる．
# 長方形と言われているからと言って必ずしも辺が異なるわけではない．

from collections import Counter
n = int(input())

A = list(map(int, input().split()))

a_cnt = Counter(A)

dup_num = []
for k, v in a_cnt.items():
    if v >= 2:
        dup_num.append(k)
    if v >= 4:
        dup_num.append(k)

dup_num.sort(reverse=True)


if len(dup_num) >= 2:
    print(dup_num[0] * dup_num[1])
else:
    print(0)