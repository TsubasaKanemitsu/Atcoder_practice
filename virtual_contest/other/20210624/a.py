n = int(input())


def is_prime(n):
    if n == 1:
        return True
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

if is_prime(n):
    print("YES")
else:
    print("NO")