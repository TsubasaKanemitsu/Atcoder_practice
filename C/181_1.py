# itertoolsで実装する簡単なbit全探索
from itertools import combinations
n = list(map(int, input()))

result = -1
flag = False
for i in range(len(n)):
    for comb in combinations(n, len(n) - i):
        if sum(comb) % 3 == 0:
            result = i
            flag = True
            break
    if flag:
        break
print(result)

