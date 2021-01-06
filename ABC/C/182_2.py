n = list(map(int, input()))

# bit全探索
def solve(n):
    INF = len(n)
    res = INF
    for bit in range(1 << len(n)):
        sum, con = 0, 0
        for i in range(len(n)):
            if bit & (1 << i):
                con += 1
            else:
                sum += n[i]
        if sum % 3 == 0:
            res = min(res, con)
    return res if res < INF else -1

print(solve(n))
