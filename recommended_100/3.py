s = input()
ans = 0
for i in range(len(s)):
    count = 0
    for j in range(i, len(s)):
        if s[j] in ['A', 'C', 'G', 'T']:
            count += 1
        else:
            break
    ans = max(ans, count)

print(ans)
