from collections import deque

n, x = list(map(int, input().split()))

tot = [0] * (n + 1)
patty = [0] * (n + 1)


def f(level, xx):
    if level == 0:
        return 1
    if xx < 1:
        return 0
    xx -= 1

    if xx < tot[level - 1]:
        return f(level - 1, xx)
    xx -= tot[level - 1]

    if xx < 1:
        return patty[level - 1] + 1

    if xx < tot[level - 1]:
        return patty[level - 1] + 1 + f(level - 1, xx)

    xx -= tot[level - 1]

    return patty[level - 1] * 2 + 1


x -= 1
tot[0] = 1
for i in range(1, n + 1):
    tot[i] = tot[i - 1] * 2 + 3

for i in range(1, n + 1):
    patty[i] = patty[i - 1] * 2 + 1

print(f(n, x))