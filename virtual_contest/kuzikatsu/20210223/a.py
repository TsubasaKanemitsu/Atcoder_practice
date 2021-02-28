b = input()
ans = ''
for i in range(len(b)):
    if b[i] == 'A':
        ans += 'T'
    elif b[i] == 'T':
        ans += 'A'
    elif b[i] == 'C':
        ans += 'G'
    else:
        ans += 'C'
print(ans)