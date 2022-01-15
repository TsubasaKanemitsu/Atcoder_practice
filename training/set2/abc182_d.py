# 35分
n = int(input())

# 進み方
# A1
# A1 + (A1 + A2)
# A1 + (A1 + A2) + (A1 + A2 + A3)
# ....
# というように進んでいく

# 1. 移動距離の算出方法
# Aの累積和でi回目の移動距離を求めることができる。
# 2. 到達位置の算出方法
# i回目の移動による到達位置はAの累積和の累積和で求めることができる。
# 難点
# i回目の移動途中における最大値を求めること
# i回目における進むことができる距離の最大値を

A = list(map(int, input().split()))


move_dist = [A[0]]
# 移動距離
for i in range(1, n):
    move_dist.append(move_dist[i - 1] + A[i])
# print(move_dist)

move_dist_max = [move_dist[0]]
for i in range(1, n):
    move_dist_max.append(max(move_dist_max[i - 1], move_dist[i]))
# print(move_dist_max)

destination = [move_dist[0]]
# 到達位置
for i in range(1, n):
    destination.append(destination[i - 1] + move_dist[i])
# print(destination)

now = 0
ans = 0
for i in range(n):
    ans = max(ans, now + move_dist_max[i])
    now = destination[i]
ans = max(ans, now)
print(ans)
