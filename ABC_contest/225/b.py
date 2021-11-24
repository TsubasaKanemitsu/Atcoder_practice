from collections import defaultdict
n = int(input())
cnt = defaultdict(int)

for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    cnt[a] += 1
    cnt[b] += 1

for i in range(1, n + 1):
    if cnt[i] == n - 1:
        print("Yes")
        exit()
print("No")