from decimal import Decimal
n, x = list(map(int, input().split()))
VP = [list(map(int, input().split())) for _ in range(n)]
alc = 0
cnt = 0
for i in range(n):
    v, p = VP[i]
    alc += Decimal(str(v)) * Decimal(str(p / 100))
    cnt += 1
    if alc > x:
        print(cnt)
        exit()
print(-1)