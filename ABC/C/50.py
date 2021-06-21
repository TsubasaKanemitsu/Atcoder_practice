from collections import Counter
n = int(input())
A = list(map(int, input().split()))

# 奇数の場合
if n % 2 == 1:
    zero = False
    pair = True
    cnt = Counter(A)
    for k, v in cnt.items():
        if k == 0 and v == 1:
            zero = True
        else:
            if v != 2:
                pair = False
    if zero and pair:
        print(pow(2, (n - 1) // 2, 10 ** 9 + 7))
    else:
        print(0)

else:
    one = False
    pair = True
    cnt = Counter(A)
    for k, v in cnt.items():
        if k == 1 and v == 2:
            one = True
        else:
            if v != 2:
                pair = False
    if one and pair:
        print(pow(2, n // 2, 10 ** 9 + 7))
    else:
        print(0)