n = int(input())
A = list(map(int, input().split()))

def lcm(x, y):
    import math
    return x * y // math.gcd(x, y)


_lcm = A[0]

for i in range(1, n):
    _lcm = lcm(_lcm, A[i])
# print(_lcm - 1)
_lcm -= 1
ans = 0
for a in A:
    ans += _lcm % a
print(ans)