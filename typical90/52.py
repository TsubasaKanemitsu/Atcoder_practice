# 12分

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

ans = 1
for i in range(n):
    ans *= sum(A[i]) % (10 ** 9 + 7)
print(ans % (10 ** 9 + 7))