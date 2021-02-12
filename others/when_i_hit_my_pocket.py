k, a, b = list(map(int, input().split()))

if b - a <= 2:
    print(k + 1)
else:
    k = k - (a - 1)
    biscket = a
    biscket += (b - a) * (k // 2)
    biscket += k % 2 
    print(biscket)