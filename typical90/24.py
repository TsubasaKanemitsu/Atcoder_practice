# 12分
# 差と偶奇の性質

n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = 0

for i in range(n):
    diff += abs(A[i] - B[i])

if k < diff:
    print("No")
elif k == diff:
    print("Yes")
else:
    if k % 2 == diff % 2:
        print("Yes")
    else:
        print("No")
