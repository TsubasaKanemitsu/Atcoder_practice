n = int(input())
s = input()
k = int(input())

word = s[k - 1]
ans = ''
for i in range(n):
    if s[i] != word:
        ans += '*'
    else:
        ans += word
print(ans)