# https://takeg.hatenadiary.jp/entry/2019/11/22/212816
import bisect
n = int(input())
L = list(map(int, input().split()))
L.sort()
# print(L)
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        index = bisect.bisect_left(L, L[i] + L[j])
        cnt += index - j - 1

print(cnt)
