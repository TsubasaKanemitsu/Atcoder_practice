from decimal import Decimal
a, b, c = list(map(int, input().split()))

a = Decimal(str(a))
b = Decimal(str(b))
c = Decimal(str(c))

left = a + b + 2 * (a * b) ** Decimal('0.5')
right = c
if left < right:
    print("Yes")
else:
    print("No")
