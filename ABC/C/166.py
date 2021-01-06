n, m = list(map(int, input().split()))

H = list(map(int, input().split()))

ans = [True for i in range(0, n)]

for i in range(m):
    a, b = list(map(int, input().split()))
    if H[a - 1] < H[b - 1]:
        ans[a - 1] = False
    elif H[a - 1] > H[b - 1]:
        ans[b - 1] = False
    else:
        ans[a - 1] = False
        ans[b - 1] = False
print(ans.count(True))