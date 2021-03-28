# 平行移動 ⇒ 回転 ⇒ 平行移動で元の位置における回転後の座標が求まる

import math

def rotate(x, y, deg):
    # theata = (180 / deg) * math.pi
    theta = math.radians(deg)
    X = x * math.cos(theta) - y * math.sin(theta)
    Y = x * math.sin(theta) + y * math.cos(theta)

    return X, Y

n = int(input())

x0, y0 = list(map(int, input().split()))
xn2, yn2 = list(map(int, input().split()))

center = ((x0 + xn2) / 2, (y0 + yn2) / 2)

# 平行移動(回転させるために(x0, y0)を原点に移動)
x, y = x0 - center[0], y0 - center[1]

deg = 360 / n
X, Y = rotate(x, y, deg)

print(X + center[0], Y + center[1])


