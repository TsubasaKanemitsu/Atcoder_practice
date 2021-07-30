# ABC 153 C
# 2分

n, k = list(map(int, input().split()))

H = list(map(int, input().split()))

H.sort(reverse=True)

if n <= k:
    print(0)
else:
    ans = sum(H[k:])
    print(ans)