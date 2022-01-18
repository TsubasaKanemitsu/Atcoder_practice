# 累積和
# 時間がかかったので、復習した方がいいかも
from collections import defaultdict
n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

# 考察1
# 連続部分列の区間和を求めたい
# 事前に累積和を求めておけば
# 区間における和をO(1)で求めることができる

# 考察2
# 区間和がKになっていればいいので
# cum_sum_A[r] - cum_sum_A[l] = k と定式化できる
# 位置rまでの地点（1 < l < r）でcum_sum_A[l] = cum_sum_A[r] - kとなる
# 値が何個出現しているかがわかれば、r地点における組み合わせの数を求めることができる

# よって、位置をずらすごとに出現する累積和をカウントしていき
# 現在値より手前に現在の累積和よりKだけ低い値の個数分だけ
# 毎回加算することで答えを求めることができる。

cum_sum_A = [A[0]]

for i in range(1, n):
    cum_sum_A.append(cum_sum_A[i - 1] + A[i])
cnt = defaultdict(int)

ans = 0
for a in cum_sum_A:
    if cnt[a - k] > 0:
        ans += cnt[a - k]
    cnt[a] += 1
    
ans += cnt[k]
print(ans)
