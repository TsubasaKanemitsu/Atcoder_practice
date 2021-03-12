# 2WA
# 45分
s = input()

cum_sum_b = [0 for _ in range(len(s) + 1)]
for i in range(1, len(s) + 1):
    if s[i - 1] == 'B':
        cum_sum_b[i]  = (cum_sum_b[i - 1] + 1)
    else:
        cum_sum_b[i] = cum_sum_b[i - 1]
ans = 0
for i in range(1, len(cum_sum_b)):
    if s[i - 1] == 'W':
        ans += cum_sum_b[i]
print(ans)
