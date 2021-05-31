from decimal import Decimal
a, b = list(input().split())

ans = Decimal(a) * Decimal(b)
print(int(ans))