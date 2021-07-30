# ABC 151C
# 4分半
# 状態管理

n, m = list(map(int, input().split()))

ac = [False] * n
wa = [0] * n
wa_cnt = [0] * n
for i in range(m):
    p, s = input().split()
    p = int(p)
    
    p -= 1
    if s == "AC":
        if ac[p] == False:
            wa[p] += wa_cnt[p]
        ac[p] = True
    else:
        wa_cnt[p] += 1
    
print(ac.count(True), sum(wa))