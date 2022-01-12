# https://kagamiz.hatenablog.com/entry/2014/12/21/213931
# マンハッタン距離
# 2次元平面におけるマンハッタン距離は4パターン存在しており
# xi > xj and yi > yj -> (xi + yi) - (xj + yj) -> xi' - xj'
# xi > xj and yi < yj -> (xi - yi) - (xj - yj) -> yi' - yj'
# xi < xj and yi < yj -> (xj + yj) - (xi + yi) -> xj' - xi'
# xi < xj and yi > yj -> (xj - yj) - (xi - yi) -> yi' - yj'
# xi + yi, xi - yiはそれぞれ
# xi' = xi + yi, yi' = xi - yi
# と置き換えると(これはx, yを45度座標回転することと同値である)
# 先ほどの4パターンを以下のようにまとめることができる
# |xi' - xj'|, |yi' - yj'|
# この4パターンのマンハッタン距離の最大値を求める際
# max(|xi' - xj'|, |yi' - yj'|)をとればいい。
# このとき, 45度回転させたx座標、y座標を用いて独立に
# 距離を求めることができるため
# 回転前はO(N^2)でしか求められなかった、
# 最大距離の計算を
# O(N)で求めることができるようになる。

n = int(input())

rotate_x = []
rotate_y = []

for _ in range(n):
    x, y = list(map(int, input().split()))
    rotate_x.append(x + y)
    rotate_y.append(x - y)

rotate_x.sort()
rotate_y.sort()

x_max_dist = abs(rotate_x[0] - rotate_x[-1])
y_max_dist = abs(rotate_y[0] - rotate_y[-1])
print(max(x_max_dist, y_max_dist))
