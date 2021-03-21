# 21分
from collections import defaultdict
n = int(input())
b = [int(input()) for _ in range(n - 1)]

money = [0, 1]
for i in range(n):
    money.append(1)

jyoushi2buka = defaultdict(list)

for i in range(n - 1):
    jyoushi2buka[b[i]].append(i + 2)

for i in range(n, 0, -1):
    buka = jyoushi2buka[i]
    if buka == []:
        pass
    else:
        min_money = 10 ** 99
        max_money = 0
        for bk in buka:
            min_money = min(min_money, money[bk])
            max_money = max(max_money, money[bk])
        money[i] += min_money + max_money
print(money[1])