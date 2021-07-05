from collections import defaultdict
n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

# 全員に配る、残りk_dash人に配る
all_, K = divmod(k, n)

candy = defaultdict(int)

aa = []
# 添え字と要素のソート
for i in range(n):
    candy[A[i]] += all_
    aa.append([i, A[i]])
aa.sort(key=lambda x:x[1])

for i in range(K):
    candy[aa[i][1]] += 1

aa.sort(key=lambda x:x[0])

for key, val in aa:
    print(candy[val])
