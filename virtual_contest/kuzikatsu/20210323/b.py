s = input()
t = input()
match_cnt = 0

for i in range(len(s) - len(t) + 1):
    cnt = 0
    for j in range(len(t)):
        if s[i + j] == t[j]:
            cnt += 1
    match_cnt = max(match_cnt, cnt)
print(len(t) - match_cnt)