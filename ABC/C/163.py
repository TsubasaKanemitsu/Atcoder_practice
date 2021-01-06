n = int(input())

A = list(map(int, input().split()))
ans = [0 for i in range(n)]
for a in A:
    ans[a - 1] += 1

for i in range(n):
    print(ans[i])