# 割り算でオーバーフローになりそうなときは，Decimal型で割り算を行う
import math
from decimal import Decimal
a, b, x = list(map(int, input().split()))

a_num = math.ceil(Decimal(str(a)) / Decimal(str(x)))
b_num = math.floor(Decimal(str(b)) / Decimal(str(x)))
print(b_num - a_num + 1)