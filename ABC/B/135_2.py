n = int(input())
p = list(map(int, input().split()))

ans = sorted(p)

count = 0
for i in range(n):
    if p[i] != ans[i]:
        count += 1

if count == 0 or count == 2:
    print("YES")
else:
    print("NO")