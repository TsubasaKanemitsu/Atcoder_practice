n = int(input())

if n == 1:
    print(0)
else:
    ans = (10 ** n - 2 * 9 ** n +  8 ** n) % (10 ** 9 + 7)
    print(ans)