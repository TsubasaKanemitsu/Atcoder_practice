s = input()

if s[0] == '0':
    ans = ''
    for i in range(len(s)):
        if i % 2 == 0:
            ans += '0'
        else:
            ans += '1'
else:
    ans = ''
    for i in range(len(s)):
        if i % 2 == 0:
            ans += '1'
        else:
            ans += '0'

cnt = 0
for i in range(len(s)):
    if s[i] != ans[i]:
        cnt += 1
print(cnt)