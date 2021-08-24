n, X = list(map(int, input().split()))
a = list(map(int, input().split()))

for bit in range(1 << n):
    num = 0
    ans = 0
    for i in range(n):
        if bit & (1 << i):
            num += 2 ** i
            ans += a[i]

    if num == X:
        print(ans)
        exit()
