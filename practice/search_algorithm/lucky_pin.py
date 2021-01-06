# 貪欲法 & 動的計画法

import itertools

n = int(input())

s = list(input())

password = [str(i).zfill(3) for i in range(0, 1000)]

count = 0
for pwd in password:
    i = 0
    for w in s:
        if w == pwd[i]:
            i += 1
        if i == 3:
            count += 1
            break

print(count)
