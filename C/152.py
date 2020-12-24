n = int(input())
P = list(map(int, input().split()))

min_val = P[0]
count = 0
for i in range(n):
    if P[i] <= min_val:
        count += 1
        min_val = P[i]

print(count)

# 条件に一致するかどうかは1 ~ jまでの数列の最小値がPiより大きいということを判定すればいい
# 最小値の値は常に更新すればいい