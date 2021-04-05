# 13分 1WA
# from decimal import Decimal
n = int(input())

# ans = Decimal(str(n)) * Decimal(str(n + 1)) / Decimal('2') - Decimal(str(n))

ans = n * (n - 1) // 2
print(ans)