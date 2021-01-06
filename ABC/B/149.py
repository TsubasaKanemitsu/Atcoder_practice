a, b, k = list(map(int, input().split()))

if a + b < k:
    print(0, 0)
elif k <= a:
    print(a - k, b)
elif a <= k <= a + b:
    print(0, b + a - k)
