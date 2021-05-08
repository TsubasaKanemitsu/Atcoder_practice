import math
n = int(input())
A = list(map(int, input().split()))


def lcm(x, y):
    return x * y // math.gcd(x, y)


_lcm = A[0]
for i in range(n):
    _lcm = lcm(_lcm, A[i])


# lcm = 1
# for k, v in lcm_dict.items():
#     lcm *= pow(k, v, 10 ** 9 + 7)

ans = 0
for i in range(n):
    ans += _lcm // A[i]
print(ans % (10 ** 9 + 7))