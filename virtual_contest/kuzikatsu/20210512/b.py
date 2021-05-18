from decimal import Decimal
n, x = list(map(int, input().split()))
VP = [list(map(int, input().split())) for _ in range(n)]
alchol = Decimal(str(0))
for i in range(n):
    v, p = VP[i]
    alchol += Decimal(str(v)) * Decimal(str(p)) / Decimal(str(100))
    if alchol > x:
        print(i + 1)
        exit()
print(-1)