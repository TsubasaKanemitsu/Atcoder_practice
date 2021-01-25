# 再復習が必要
from collections import defaultdict
n, m = list(map(int, input().split()))

wa_count = 0
ac_count = 0
q_dict = defaultdict(int)
wa_dict = defaultdict(int)
for i in range(m):
    p, s = list(input().split())
    p = int(p)
    if q_dict[p] == False:
        if s == 'AC':
            q_dict[p] = True
            ac_count += 1
            wa_count += wa_dict[p]
        else:
            wa_dict[p] += 1

print(ac_count, wa_count)
# 考察
# ACを1回以上出した問題においてのACとWAの総和を出すということなので
# ACが出ていない状況でのみAC数とWA数は増加する
# これは核問題でACが出ているかどうかをTrue, Falseで辞書として保持しておく
# ACは初めてACが出たときだけ+1加算され，WAはACが出るまでは加算されつづけるので，
# s == 'AC'とs == 'WA'で分類し，WAのときは常にWA数を増加させ，ACになった時に，そのWA数をACが出た問題におけるWA数と
# すればいい．