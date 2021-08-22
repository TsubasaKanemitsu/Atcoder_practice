s = input()

cnt = 0
color = s[0]
for i in range(len(s)):
    if color != s[i]:
        cnt += 1
    color = s[i]
print(cnt)