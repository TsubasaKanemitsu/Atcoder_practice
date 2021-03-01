# 3分
# 誤差系の問題は，Decimalモジュールを使用する
from decimal import Decimal

a, b = list(input().split())
b = b.split('.')
b = ''.join(b)
a, b = int(a), int(b)
print(a * b // 100)

# a = Decimal(a)
# b = Decimal(b)
# print(int(a * b))

