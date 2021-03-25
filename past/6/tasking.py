from collections import defaultdict
n = int(input())

data = defaultdict(list)

for i in range(n):
    a, b = list(map(int, input().split()))
    data[a].append(b)

cnt = [0] * 101
ans = 0
for i in range(1, n + 1):
    # i日目まで実行可能なタスク
    # bはタスクの値
    for b in data[i]:
        cnt[b] += 1

    for b in range(100, 0, - 1):
        if cnt[b] > 0:
            ans += b
            cnt[b] -= 1
            break
    print(ans)