n = int(input())


def is_prime(x):
    if x == 1:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


if is_prime(n):
    print("YES")
else:
    print("NO")