# combinationは遅い
# 定数倍の見積
# 掛け算で値が大きくなる時は毎回剰余を求める

N, P, Q = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = 0

for i in range(N):
    val = 1
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            for l in range(k + 1, N):
                for m in range(l + 1, N):
                    val = A[i] % P * A[j] % P * A[k] % P * A[l] % P * A[m] % P
                    if val % P == Q:
                        ans += 1
print(ans)