# 25分
# 最小値更新
n = int(input())
P = list(map(int, input().split()))

# iより手前のどの数字よりも小さいPiとなるときのiの個数を求める
# 現在の最大値を常に更新しつつ、その最大値よりPiが小さいかを判定する

# 自分より手前の数値よりも小さいときに、数え上げ + 最小値の更新を行う
min_ = P[0]
ans = 0
for i in range(n):
    if min_ >= P[i]:
        ans += 1
        min_ = P[i]
print(ans)