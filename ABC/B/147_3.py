s = input()
n = len(s)
count = 0
for i in range(len(s)//2):
    if s[i] != s[n - 1 - i]:
        count += 1
print(count)