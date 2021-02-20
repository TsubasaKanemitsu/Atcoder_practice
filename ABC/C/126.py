# 13分
n, k = list(map(int, input().split()))

card_exv = 1 / n
coin_exv = 1 / 2


def over_k_cnt(xx, k):
    cnt = 0
    i = xx
    while i < k:
        i *= 2
        cnt += 1
    return cnt


prob = 0
for i in range(1, n + 1):
    prob += card_exv * coin_exv ** over_k_cnt(i, k)
print(prob)