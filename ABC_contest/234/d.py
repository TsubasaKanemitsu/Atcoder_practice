# https://atcoder.jp/contests/abc234/editorial/3222

import heapq
n, k = list(map(int, input().split()))
P = list(map(int, input().split()))

# 先頭からi番目までのPiの中で
# K番目に大きい値がわかればいい

# 先頭からi番目までのsortされた状態がわかるとうれしい
# 愚直に毎回sortをすると
# O(N^2logN)となり、TLEとなる

# heapqを使う
# O(Nlogk)

# number = P[0:k]
# heapq.heapify(number)
# now = 10 ** 18
# ans = []
# for i in range(n - k):
#     now = heapq.heappop(number)
    
#     if P[k + i] > now:
#         heapq.heappush(number, P[k + i])
        
#     else:
#         heapq.heappush(number, now)
#     ans.append(now)
# now = heapq.heappop(number)
# ans.append(now)
# for a in ans:
#     print(a)


que = P[0:k]
heapq.heapify(que)
print(min(que))
for i in range(k, n):
    min_max = heapq.heappop(que)
    min_max = max(min_max, P[i])
    heapq.heappush(que, min_max)
    ans = heapq.heappop(que)
    print(ans)
    heapq.heappush(que, ans)
