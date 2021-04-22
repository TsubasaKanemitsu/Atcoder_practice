# 20分
# 組み合わせ総数
def combinations_count(n, r):
    import math
    return math.factorial(n) // ((math.factorial(n - r)) * math.factorial(r))

w, h = list(map(int, input().split()))
w -= 1
h -= 1
ans = combinations_count(w + h, h)
print(ans % (10 ** 9 + 7))
