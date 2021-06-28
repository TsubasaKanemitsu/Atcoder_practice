a, b, c = list(map(int, input().split()))

ans = 0
while True:
    b -= a
    if b >= 0 and ans < c:
        ans += 1
    else:
        print(ans)
        exit()