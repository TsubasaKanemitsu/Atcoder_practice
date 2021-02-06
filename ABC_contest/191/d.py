import math
from decimal import Decimal

x, y, r = map(Decimal, input().split())

high_y = math.floor(y + r)
low_y = math.ceil(y - r)

count = 0
for i in range(low_y, high_y + 1):
    p = Decimal(r ** 2 - (y - i) ** 2).sqrt()
    high = math.floor(x + p)
    low = math.ceil(x - p)
    count += high - low + 1
    
print(count)

