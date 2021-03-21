# 22分
# 3WA
# この問題では，数値を平方根にするときの値の変換に誤差が発生することで
# 最終的な数値計算の誤差が発生する
# Decimal型を利用することで計算誤差をなくす
# 平方根化もDecimalのモジュールで行う
# sqrt() 最大精度の平方根

from decimal import Decimal

a, b, c = list(map(int, input().split()))

a = Decimal(str(a)).sqrt()
b = Decimal(str(b)).sqrt()
c = Decimal(str(c)).sqrt()

if a + b < c:
    print("Yes")
else:
    print("No")
