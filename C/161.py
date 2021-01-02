n, k = list(map(int, input().split()))
count = 0

div = n // k
r = n % k

if r == 0:
    print(0)
else:
    ans = min(r, abs(r - k))
    print(ans)