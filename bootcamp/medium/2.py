# 3分30秒

s = input()

b_cnt = 0
ans = 0

for i in range(len(s)):
    if s[i] == 'B':
        b_cnt += 1
    else:
        ans += b_cnt

print(ans)