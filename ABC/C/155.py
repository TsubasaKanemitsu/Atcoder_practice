n = int(input())
s = dict()

for i in range(n):
    word = input()
    if word not in s:
        s[word] = 1
    else:
        s[word] += 1
max_val = max(s.values())

ans = list()
for key, value in s.items():
    if value == max_val:
        ans.append(key)
ans.sort()

for i in ans:
    print(i)