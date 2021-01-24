n, x = list(map(int, input().split()))

ans = []
for i in range(n):
    v, p = list(map(int, input().split()))
    ans.append(v * p)
    
# print(ans)
cum_ans = [ans[0]]

for i in range(1, n):
    cum_ans.append(cum_ans[i - 1] + ans[i])
    
for i in range(n):
    if (cum_ans[i] / 100) > x:
        print(i + 1)
        exit()
print(-1)