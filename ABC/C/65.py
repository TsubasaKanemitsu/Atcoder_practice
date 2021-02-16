# 22分
# 参考 https://img.atcoder.jp/arc076/editorial.pdf
n, m = list(map(int, input().split()))

def permutaions_count(n, r):
    import math
    return math.factorial(n) // math.factorial(n - r)

if abs(n - m) > 1:
    print(0)
    exit()
else:
    if n % 2 == 0 and m % 2 == 0:
        ans = 2 * permutaions_count(n, n) * permutaions_count(m, m) % (10 ** 9 + 7)
    elif n % 2 == 0 and m % 2 == 1:
        ans = permutaions_count(n, n) * permutaions_count(m, m) % (10 ** 9 + 7)
    elif n % 2 == 1 and m % 2 == 0:
        ans = permutaions_count(n, n) * permutaions_count(m, m) % (10 ** 9 + 7)
    elif n % 2 == 1 and m % 2 == 1:
        ans = 2 * permutaions_count(n, n) * permutaions_count(m, m) % (10 ** 9 + 7)
    print(ans)