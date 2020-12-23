# 10進数をn進数に変換
def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

# 重複なし3重ループ
def triple_roop(n):
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                print(i, j, k)

# 素数判定
def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# 約数列挙
def divisor(n):
    i = 1
    divisor_list = []
    while i * i <= n:
        if n % i == 0:
            divisor_list.append(i)
            if n // i != i:
                divisor_list.append(n // i)
        i += 1
    divisor_list.sort()
    return divisor_list

# 最大公約数
# mathライブラリのmath.gcd(x, y)も使える
def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b > 0:
        a, b = b, a % b

    return b

# 最小公倍数
def lcm(x, y):
    import math
    return (x * y) // math.gcd(x, y)
