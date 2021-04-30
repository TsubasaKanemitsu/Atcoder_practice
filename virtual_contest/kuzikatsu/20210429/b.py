n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
sm_a = sum(a)
num = sm_a / (4 * m)

cnt = 0
for i in range(n):
    if a[i] >= num:
        cnt += 1

if cnt >= m:
    print("Yes")
else:
    print("No")