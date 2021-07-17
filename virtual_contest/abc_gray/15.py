# ABC 144C
# 掛け算の組み合わせのうち、x * y = n
# となるもののうち、x, yの差が小さいものほど最小の移動回数で到達できる

# 4分

n = int(input())

def divisor(n):
    # if n == 1:
    #     return
    res = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            res.append([i, n // i])

        i += 1
    
    return res

res = divisor(n)

ans = sum(res[-1]) - 2
print(ans)