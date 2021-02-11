n = int(input())
work = []
a = []
b = []

for i in range(n):
    _a, _b = list(map(int, input().split()))
    work.append([_a, _b])
    
work = sorted(work, key=lambda x: x[1])

time_cum_sum = [work[0][0]]
for i in range(1, len(work)):
    time_cum_sum.append(time_cum_sum[i - 1] + work[i][0])

for i in range(len(work)):
    if time_cum_sum[i] > work[i][1]:
        print("No")
        exit()
print("Yes")