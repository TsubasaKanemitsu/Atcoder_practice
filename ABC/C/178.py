n = int(input())

def powmod(num, n):
    return num ** n

mod = 10 ** 9 + 7

ans = powmod(10, n) - 2 * powmod(9, n) + powmod(8, n)
print(ans % mod)