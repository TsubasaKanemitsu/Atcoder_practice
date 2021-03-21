x, y = list(map(int, input().split()))

if (x > 0 and y < 0):
    ans = abs(x - -1 * y) + 1
    print(ans)
elif (x < 0 and y > 0):
    ans = abs(y - - 1 * x) + 1
    print(ans)

elif x < 0 and y < 0 and x > y:
    ans = abs(x - y) + 2
    print(ans)
elif x < 0 and y < 0 and x < y:
    ans = abs(x - y)
    print(ans)

elif x > 0 and y > 0 and x > y:
    ans = abs(x - y) + 2
    print(ans)
elif x > 0 and y > 0 and x < y:
    ans = abs(x - y)
    print(ans)

elif x == 0 and y < 0:
    ans = abs(y) + 1
    print(ans)
elif x > 0 and y == 0:
    ans = x + 1
    print(ans)
else:
    ans = abs(x - y)
    print(ans)
