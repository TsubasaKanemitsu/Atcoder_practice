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

num = x
while True:
    judge = is_prime(num)
    if judge:
        ans = num
        break
    num += 1

print(ans)