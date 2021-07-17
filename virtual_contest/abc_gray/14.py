# ABC 143C
# 8分30秒
# 1WA

n = int(input())
s = list(input())

cnt = 1
now = s[0]
for i in range(n):
    if now != s[i]:
        cnt += 1
        now = s[i]
print(cnt)