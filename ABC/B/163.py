N, M = list(map(int, input().split()))

A = list(map(int, input().split()))

sm_day = sum(A)

if N < sm_day:
    print(-1)
else:
    print(N - sm_day)