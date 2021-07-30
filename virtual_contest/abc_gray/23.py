# 6分
from collections import defaultdict
n = int(input())
S = [input() for _ in range(n)]

cnt = defaultdict(int)

for i in range(n):
    cnt[S[i]] += 1

array = list(cnt.items())
array.sort(key=lambda x:(x[1]), reverse=True)
max_val = array[0][1]

word = []
for i in range(len(array)):
    if array[i][1] == max_val:
        word.append(array[i][0])

word.sort()
for w in word:
    print(w)