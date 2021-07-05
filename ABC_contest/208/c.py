from collections import defaultdict
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

all_ = 0
while k > 0:
    if k >= n:
        all_ += (k // n)
        k -= n * (k // n)
    else:
        break
ac = []
candy = defaultdict(int)
for i in range(n):
    # i人目, 国民番号, 雨の数
    ac.append([i, a[i]])
    candy[a[i]] += all_
ac.sort(key=lambda x:x[1])


for kk in range(k):
    num = ac[kk][1]
    candy[num] += 1
ac.sort(key=lambda x:x[0])
for i in range(n):
    print(candy[ac[i][1]])