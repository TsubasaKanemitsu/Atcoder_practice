s = input()
l = len(s)
ans = 0
for i in range(l - 2, 0, -2):
    j = i // 2
    a = s[0:j]
    b = s[j:i]
    # print(a, b)
    if a == b:
        ans = j*2
        break

print(ans)

