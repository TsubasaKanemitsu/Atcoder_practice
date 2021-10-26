x, y = list(map(int, input().split()))

if x == y:
    print(x)
else:
    all_ = set({0, 1, 2})
    ans = list(all_ - set({x, y}))[0]
    print(ans)
