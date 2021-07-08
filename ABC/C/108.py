n, k = list(map(int, input().split()))

ans1 = 0
ans2 = 0
for i in range(1, n + 1):
    if i % k == 0:
        ans1 += 1
        
    elif i % k == k / 2 and k % 2 == 0:
        ans2 += 1
        
ans = ans1 ** 3 + ans2 ** 3
print(ans)