n = int(input())
s = list(input())
t = list(input())

cnt = 0

match_num = 0
for i in range(n):
    ss = s[i:]
    num = len(ss)
    cnt = 0
    for j in range(len(ss)):
        if ss[j] == t[j]:
            cnt += 1
    if cnt == num:
        match_num = num
        break

ans = (n - match_num) * 2 + match_num
print(ans)