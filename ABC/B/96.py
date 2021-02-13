a, b, c = list(map(int, input().split()))
k = int(input())

ans = 2 * max(a, b, c)
if a >= b and a >= c:
    ans = a * 2 ** k + b + c
elif b >= a and b >= c:
    ans = b * 2 ** k + a + c
elif c >= a and c >= b:
    ans = c * 2 ** k + a + b
print(ans)