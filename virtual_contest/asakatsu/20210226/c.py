n, q = list(map(int, input().split()))
s = input()

LR = [list(map(int, input().split())) for _ in range(q)]

cum_sum = [0] 
for i in range(n - 1):
    if s[i] == 'A' and s[i + 1] == 'C':
        cum_sum.append(cum_sum[i] + 1)
    else:
        cum_sum.append(cum_sum[i])       

for lr in LR:
    print(cum_sum[lr[1] - 1] - cum_sum[lr[0] - 1])
