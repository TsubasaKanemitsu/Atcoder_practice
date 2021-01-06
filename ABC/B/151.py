n, k, m = list(map(int, input().split()))
A = list(map(int, input().split()))

# 理想の合計点(最低)
sm_score = n * m

A_score = sum(A)

if sm_score - A_score > k:
    print(-1)
elif A_score >= sm_score:
    print(0)
else:
    print(sm_score - A_score)
