s = input()

ans = []
for i in range(len(s)):
    if s[i] == 'B' and len(ans) == 0:
        pass
    elif s[i] == 'B' and len(ans) >= 1:
        ans.pop()
    else:
        ans.append(s[i])
print(''.join(ans))