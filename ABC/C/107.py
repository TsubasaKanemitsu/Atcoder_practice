n, k = list(map(int, input().split()))
x = list(map(int, input().split()))

x = [xx for xx in x]

ans = 10 ** 99
for i in range(n - k + 1):
    j = i + (k - 1)
    
    if x[i] <= 0 and x[j] > 0:
        ans = min(ans, min(abs(x[i]), x[j]) * 2 + max(abs(x[i]), x[j]))
    elif x[i] <= 0 and x[j] <= 0:
        ans = min(ans, abs(x[i]))
    else:
        ans = min(ans, x[j])
if ans == 10 ** 99:
    print(0)
    exit()
print(ans)