n, m = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

ans = A ^ B
ans = sorted(ans)
for a in ans:
    print(a, end=" ")