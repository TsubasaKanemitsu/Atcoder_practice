n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sum(a) < sum(b):
    print(-1)
    exit()

diff = []
for i in range(n):
    diff.append(a[i] - b[i])

minus = []
plus = []
for i in range(n):
    if diff[i] < 0:
        minus.append(diff[i])
    elif diff[i] >= 0:
        plus.append(diff[i])

cnt = len(minus)
sum_minus = sum(minus)
plus.sort(reverse=True)
if sum_minus == 0:
    print(0)
    exit()
else:
    for i in range(len(plus)):
        sum_minus += plus[i]
        cnt += 1
        if sum_minus >= 0:
            break
    print(cnt)