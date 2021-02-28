from decimal import Decimal
import math
a, b = input().split()
a = Decimal(a)
b = Decimal(b)
ans = math.floor(a * b)
print(ans)