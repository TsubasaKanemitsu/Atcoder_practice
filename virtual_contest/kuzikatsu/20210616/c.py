# 計算量のオーダを考えるのが遅かった
x = int(input())

ans = 0
for i in range(1, 10 ** 6 + 1):
    ans = ans + i
    if ans >= x:
        print(i)
        exit()