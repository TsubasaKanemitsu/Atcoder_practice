s = input()

n = len(s) + 1

ans = [0] * n

for i in range(len(s)):
    if s[i] == '<':
        ans[i + 1] = ans[i] + 1

for i in range(len(s) - 1, -1, -1):
    if s[i] == '>':
        ans[i] = max(ans[i + 1] + 1, ans[i])
print(sum(ans))