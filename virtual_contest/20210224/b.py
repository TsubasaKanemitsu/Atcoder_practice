x = int(input())

def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if (n % i) == 0:
            return False
        i += 1
    return True

while is_prime(x) == False:
    x += 1
print(x)