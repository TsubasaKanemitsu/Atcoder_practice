n, m = list(map(int, input().split()))

wa = [0] * (n + 1)
ac = [False] * (n + 1)

for _ in range(m):
    p, s = input().split()
    p = int(p)
    if s == "AC":
        ac[p] = True
    
    if not ac[p]:
        wa[p] += 1

wa_cnt = 0
ac_cnt = 0

for i in range(1, n + 1):
    if ac[i]:
        ac_cnt += 1
        wa_cnt += wa[i]
print(ac_cnt, wa_cnt)