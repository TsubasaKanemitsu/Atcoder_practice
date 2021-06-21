n = int(input())

def divisor(n):
    i = 1
    res = []
    while i * i <= n:
        temp = []
        if n % i == 0 and n % (n // i) == 0:
            temp = (str(i), str(n // i))
            res.append(temp)
        i += 1
    return res


def f(a, b):
    len_a = len(a)
    len_b = len(b)

    return max(len_a, len_b)


ans = 10 ** 99
for a, b in divisor(n):
    r = f(a, b)
    ans = min(ans, r)
print(ans)