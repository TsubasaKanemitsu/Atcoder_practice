# 7分
from collections import Counter

n = int(input())
S = [input() for _ in range(n)]

ans = Counter(S[0])

for i in range(1, n):
    ans = ans & Counter(S[i])

word = ''

for k, v in ans.items():
    word += k * v
print(''.join(sorted(word)))