# 21分
import itertools
n = int(input())

S = [input() for _ in range(n)]

m = len([s for s in S if s[0] == 'M'])
a = len([s for s in S if s[0] == 'A'])
r = len([s for s in S if s[0] == 'R'])
c = len([s for s in S if s[0] == 'C'])
h = len([s for s in S if s[0] == 'H'])

name = [m, a, r, c, h]
cnt = 0
for comb in itertools.combinations(name, 3):
    cnt += comb[0] * comb[1] * comb[2]
print(cnt)
