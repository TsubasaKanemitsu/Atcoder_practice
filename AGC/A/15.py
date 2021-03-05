# 場合分け
# 計算しえる結果の数を意識する

n, a, b = list(map(int, input().split()))

if n == 1:
    if a != b:
        print(0)
        exit()
    else:
        print(1)
        exit()

if a > b:
    print(0)
elif a == b:
    print(1)
    exit()
else:
    print((b - a)*(n - 2) + 1)