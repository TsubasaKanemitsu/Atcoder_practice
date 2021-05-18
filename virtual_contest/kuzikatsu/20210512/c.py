import math
t, N = list(map(int, input().split()))

ans = []
for i in range(100):
    if math.floor((100 + t) * i / 100) != i:
        print(math.floor((100 + t) * i / 100), i)
        ans.append(i)
print(ans[0:N])
print(ans[N])