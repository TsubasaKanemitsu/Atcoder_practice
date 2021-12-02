# 15分

from collections import deque
n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

# 条件を満たす区間和を求める
# 尺取り法


Q = deque()

right = 0
sum = 0
ans = 0
for i in range(n):
    left = i
    # 右端がNまで、プラスで必要となる条件を付け加える
    while right < n and sum < k:
        sum += A[right]
        right += 1
    # どういう条件でカウントするのか
    if sum >= k:
        # kを超える左端~右端を知ることができれば、それ以降に右に選べるaiがある分だけ
        # 部分列を作ることができるので(n - right + 1)を足している
        ans += (n - right + 1)
    # 区間の状態を更新する
    sum -= A[left]

print(ans)