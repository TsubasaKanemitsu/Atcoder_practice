# 解説AC
# atan2の仕様
# 三角関数の値の調整ができていなかった
# 俯角の求め方のイメージは大体できていた.
import math
T = int(input())
L, X, Y = list(map(int, input().split()))
Q = int(input())
E = [int(input()) for _ in range(Q)]

for e in E:
    # 1分あたりに移動する角度
    theta = e / T * 360
    y = - L / 2 * math.sin(math.radians(theta))
    z = L / 2 - L / 2 * math.cos(math.radians(theta))
    degree = math.degrees(math.atan2(z, math.sqrt(X ** 2 + abs(Y - y) ** 2)))
    print(degree)