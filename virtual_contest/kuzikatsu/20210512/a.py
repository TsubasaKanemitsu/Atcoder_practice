n, k, m = list(map(int, input().split()))
a = list(map(int, input().split()))

mean_score = n * m

ans = mean_score - sum(a)
if ans < 0:
    print(0)
elif ans > k:
    print(-1)
else:
    print(ans)