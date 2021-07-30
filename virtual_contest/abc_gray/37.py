# ABC 180C 
# 3min
# 約数列挙
n = int(input())

def div(n):
    i = 1
    res = []
    while i * i <= n:
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n // i)

        i += 1
    return res

ans = div(n)

ans.sort()
for a in ans:
    print(a)