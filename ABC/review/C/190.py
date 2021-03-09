import itertools
n, m = list(map(int, input().split()))

AB = [list(map(int, input().split())) for _ in range(m)]

k = int(input())
CD = [list(map(int, input().split())) for _ in range(k)]

ans = 0
for comb in itertools.product(*CD):
    cnt = 0
    comb = set(comb)
    for i in range(m):
        if set(AB[i]) <= comb:
            cnt += 1
    ans = max(ans, cnt)
print(ans)