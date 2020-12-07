import math
a, b, angle_c = list(map(float, input().split()))
pi = 3.141592653589793
rad = pi * angle_c / 180
R = a / (2.0 * math.sin(rad))
L = (a ** 2.0 + b ** 2.0 - 2.0 * a * b * math.cos(rad)) ** 0.5 + a + b

S = a * b * math.sin(rad) / 2.0
h = 2 * S / a

print('{:.10}'.format(S))
print('{:.10}'.format(L))
print('{:.10}'.format(h))

# めっちゃ時間かかった
# 高校数学復習が必要
# mathライブラリを使用していると，小数点以下の計算でテストをパスしないことがある
