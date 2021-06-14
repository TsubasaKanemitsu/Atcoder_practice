x, y = list(map(int, input().split()))

num = set({x, y})
i = set({0, 1, 2})
if len(num) == 1:
    ans = x
    print(ans)
elif len(num) == 2:
    ans = list(i - num)[0]
    print(ans)