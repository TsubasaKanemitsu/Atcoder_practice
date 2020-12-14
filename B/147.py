s = list(input())

l = len(s)
count = 0
if l % 2 == 0:
    a = s[0:l // 2]
    b = list(reversed(s[l // 2:]))
    for i in range(l // 2):
        if a[i] != b[i]:
            count += 1

else:
    a = s[0:(l - 1) // 2]
    b = list(reversed(s[(l + 1) // 2:]))
    for i in range((l - 1) // 2):
        if a[i] != b[i]:
            count += 1
print(count)
