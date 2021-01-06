x, k, d = list(map(int, input().split()))
x = abs(x)


def solve_axis(x, k, d):
    q = x // d
    r = x % d

    if q >= k:
        return x - d * k
    rem = k - q
    if rem % 2 == 0:
        return r
    else:
        return d - r


print(solve_axis(x, k, d))
