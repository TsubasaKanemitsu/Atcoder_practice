# ABC 187 C
# 7分
# set
from collections import defaultdict
n = int(input())

cnt = defaultdict(int)
s_set = set()

for i in range(n):
    s = input()
    if s[0] == '!':
        cnt[s[1:]] += 1
    else:
        s_set.add(s)

for ss in list(s_set):
    if cnt[ss] >= 1:
        print(ss)
        exit()
print("satisfiable")