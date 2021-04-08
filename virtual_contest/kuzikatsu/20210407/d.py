from decimal import Decimal
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

b = [0] * n
front_b = [0] * n
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if a[i] > a[j]:
            b[i] += 1
        if i > j and a[i] > a[j]:
            front_b[i] += 1

ans = 0
for i in range(n):
    # 同グループ内の転倒数
    ans += (b[i] - front_b[i]) * k
    # 他グループの転倒数
    ans += Decimal(str(k)) * Decimal(str(k - 1)) / 2 * Decimal(str(b[i]))
    
print(ans % (10 ** 9 + 7))

