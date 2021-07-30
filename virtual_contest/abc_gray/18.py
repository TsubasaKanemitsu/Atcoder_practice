
# ABC 149C
# 素数判定
# 2分探索でも可能


x = int(input())


def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


for i in range(x, 10 ** 6 + 1):
    if is_prime(i):
        print(i)
        exit()

