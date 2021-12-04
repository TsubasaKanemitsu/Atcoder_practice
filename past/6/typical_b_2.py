n = int(input())

AB = [list(map(int, input().split())) for _ in range(n)]

AB.sort(key=lambda x:x[1])

# 貪欲法
# 速く終わらせることができるタスクから順番に終わらせていく
# 現在までにタスクを完了した日付が、タスクを開始する日付より手前の場合
# 新しいタスクを実行する。
# そうでない場合は、タスクを実行しない
# 数式
# a < day -> 実行しない
# a >= day -> 実行

day = 0
ans = 0
for a, b in AB:
    if a >= day:
        ans += 1
        day = b
print(ans)