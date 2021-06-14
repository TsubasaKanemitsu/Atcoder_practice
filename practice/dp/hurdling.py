N, L = list(map(int, input().split()))
x = list(map(int, input().split()))
t1, t2, t3 = list(map(int, input().split()))

time = [10 ** 18 + 1] * (L + 1)
time[0] = 0
xx = set(x)

# start この部分のロジックは書けていた
for Di in range(1, L + 1):
    if Di >= 1:
        add = t1
        time[Di] = min(time[Di], time[Di - 1] + add)
    
    if Di >= 2:
        add = t1 + t2
        time[Di] = min(time[Di], time[Di - 2] + add)
    
    if Di >= 4:
        add = t1 + 3 * t2
        time[Di] = min(time[Di], time[Di - 4] + add)
    
    if Di in xx:
        time[Di] += t3

ans = time[L]
# end


# 答えは座標Lにピッタリ到着する or L-3, L-2, L-1からジャンプ中にゴールするか
# この部分の立式ができなかった.
for i in [L - 3, L - 2, L - 1]:
    if i >= 0:
        ans = min(ans, time[i] + t1 // 2 + t2 * (2 * (L - i) - 1) // 2)
print(ans)