# 18min
# 考察
# 高橋君の決めた新たなアルファベット順に基づく辞書順で文字を並び変える
# 順番通りに文字列を置き換えて、再度戻せばいい。

from collections import defaultdict
X = input()
n = int(input())
SS = [list(input()) for _ in range(n)]

n_order = defaultdict(str)
w_order = defaultdict(str)
for i, x in enumerate(X):
    n_order[x] = chr(ord('a') + i)
    w_order[chr(ord('a') + i)] = x

for i, S in enumerate(SS):
    for j in range(len(S)):
        SS[i][j] = n_order[S[j]]

XX = []
for S in SS:
    XX.append(''.join(S))
XX.sort()

YY = []
for X in XX:
    YY.append(list(X))

for i, Y in enumerate(YY):
    for j in range(len(Y)):
        YY[i][j] = w_order[Y[j]]

for Y in YY:
    print(''.join(Y))