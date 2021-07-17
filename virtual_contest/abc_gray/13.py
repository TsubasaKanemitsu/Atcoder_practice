# ABC142 C
# 二次元配列ソート
# 6分

n = int(input())
A = list(map(int, input().split()))

ans = []
for i, a in enumerate(A):
    ans.append([a, i])

ans.sort()
for i in range(n):
    a, i = ans[i]
    print(i + 1, end=" ")
