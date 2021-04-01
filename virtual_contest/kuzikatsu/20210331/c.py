k, a, b = list(map(int, input().split()))


if a > b:
    biscket = k + 1
elif b - a < 2:
    biscket = k + 1
else:
    if k <= 3:
        biscket = 1 + k
    else:
        k -= (a - 1)
        biscket = a + k // 2 * (b - a) + k % 2
print(biscket)