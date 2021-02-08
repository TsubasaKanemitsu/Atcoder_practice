q, h, s, d = list(map(int, input().split()))
n = int(input())

one_liter = min(4 * q, 2 * h, s)

if n == 1:
    print(one_liter)
else:
    ss = n * one_liter
    dd = (n // 2) * min(8 * q, 4 * d, 2 * s, d)
    if n % 2 == 1:
        dd += one_liter
    print(min(ss, dd))