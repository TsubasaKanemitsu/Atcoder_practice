n = int(input())
k = int(input())
x = list(map(int, input().split()))

d_sum = 0
for i in range(n):
    if x[i] >= k - x[i]:
        d_sum += (k - x[i]) * 2
    else:
        d_sum += x[i] * 2

print(d_sum)