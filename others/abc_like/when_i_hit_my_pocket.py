k, a, b = list(map(int, input().split()))

if b - a <= 2:
    print(k + 1)
else:
    k = k - (a - 1)
    biscket = a
    biscket += (b - a) * (k // 2)
    # 偶数回なら0, 奇数回なら+1回ビスケットを叩ける
    biscket += k % 2 
    print(biscket)