# CODEFESTIVAL 2015 予選A
# 19 min

# 考察
# なるべくAiを選び、Biを少なくしたい
# AiからBiに変更したときに差が大きい問題を移す問題として選択すれば
# 時間短縮につながる.

# Keyword
# 操作の変更前後の差
# 貪欲法

n, t = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(n)]

diff = []
sum_a = sum([a for a, b in AB])
for i in range(n):
    a, b = AB[i]
    diff.append(a - b)
diff.sort(reverse=True)

if sum_a <= t:
    print(0)
    exit()
for i in range(n):
    sum_a -= diff[i]
    if sum_a <= t:
        print(i + 1)
        exit()
print(-1)
