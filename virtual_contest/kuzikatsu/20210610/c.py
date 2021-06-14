from collections import defaultdict
n, m = list(map(int, input().split()))
S = [list(input()) for _ in range(n)]

cnt = defaultdict(int)
for i in range(n):
    num = 0
    for j in range(m):
        if S[i][j] == '0':
            num -= 1
        else:
            num += 1
    cnt[i + 1] = num

print(cnt)
res = 0
array = list(cnt.items())
for i in range(len(array)):
    k1, v1 = array[i]
    for j in range(i + 1, len(array)):
        k2, v2 = array[j]
        if k1 != k2 and v1 != v2:
            res += 1
print(res)