from collections import defaultdict
n = int(input())

task = defaultdict(list)


for _ in range(n):
    a, b = list(map(int, input().split()))
    # a日目にあるタスクを追加
    task[a].append(b)

cnt = defaultdict(int)


ans = 0
for day in range(1, n + 1):
    for p in task[day]:
        # タスク数の管理
        # pポイントのタスクを追加
        cnt[p] += 1

    # 点数の高いタスクから消費する
    for p in range(100, -1, -1):
        if cnt[p] > 0:
            ans += p
            cnt[p] -= 1
            break
    print(ans)