# ABC 154C
# 1分
n = int(input())
A = list(map(int, input().split()))

if len(set(A)) == n:
    print("YES")
else:
    print("NO")