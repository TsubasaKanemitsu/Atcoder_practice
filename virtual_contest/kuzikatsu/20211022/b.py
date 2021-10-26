n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
sm_a = sum(A)
cnt = 0
for a in A:
    if a >= 1 / (4 * m) * sm_a:
        cnt += 1
if cnt >= m:
    print("Yes")
else:
    print("No")