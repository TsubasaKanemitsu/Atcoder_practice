n = int(input())

def factorization(n):
    i = 2
    ans = []
    while i * i <= n:
        ex = 0
        while n % i == 0:
            n = n // i
            ex += 1
        ans.append((i, ex))
        i += 1

    if n != 1:
        ans.append((n, 1))

    return ans


ans = factorization(n)

num = 0
for a, b in ans:
    num += b
for i in range(20):
    if 2 ** i >= num:
        print(i)
        exit()