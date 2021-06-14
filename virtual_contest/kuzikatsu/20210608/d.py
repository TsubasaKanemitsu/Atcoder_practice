from collections import defaultdict
n, k = list(map(int, input().split()))

cnt = defaultdict(int)

for _ in range(n):
    a, b = list(map(int, input().split()))
    cnt[a] += b

cnt_list = list(cnt.items())
cnt_list.sort()

num = 0
for i in range(n):
    num += cnt_list[i][1]
    if num >= k:
        print(cnt_list[i][0])
        exit()