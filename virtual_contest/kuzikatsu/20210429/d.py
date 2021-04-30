Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]


def is_prime(n):
    if n == 1:
        return False
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

last = 10 ** 5
num = [0] * (last + 1)
for i in range(2, last + 1):
    if is_prime(i) and is_prime((i + 1) // 2):
        num[i] = 1

cum_num = [num[0]]

for i in range(1, len(num)):
    cum_num.append(cum_num[i - 1] + num[i])

for i in range(Q):
    l, r = LR[i]
    ans = cum_num[r] - cum_num[l - 1]
    print(ans)