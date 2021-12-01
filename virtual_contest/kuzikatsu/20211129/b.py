s = input()

ans = 0

word = {'A', 'C', 'G', 'T'}

left = 0
right = 0


for i in range(len(s)):
    if s[i] not in word:
        continue
    num = 1
    for j in range(i + 1, len(s)):
        if s[j] not in word:
            break
        num += 1
    ans = max(ans, num)
print(ans)
        
