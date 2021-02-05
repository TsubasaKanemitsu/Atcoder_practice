n, s = list(input().split())
n = int(n)
ans = 0
for i in range(n):
    count1 = 0
    count2 = 0
    for j in range(i, n):
        if s[j] == 'A':
            count1 += 1
        elif s[j] == 'T':
            count1 -= 1
        elif s[j] == 'C':
            count2 += 1
        elif s[j] == 'G':
            count2 -= 1
        if count1 == 0 and count2 == 0:
            ans += 1
print(ans)