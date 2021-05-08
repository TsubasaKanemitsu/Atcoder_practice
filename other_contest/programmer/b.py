n, m = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

ans = A ^ B
ans = list(ans)
ans.sort()
for i in range(len(ans)):
    print(ans[i], end=' ')