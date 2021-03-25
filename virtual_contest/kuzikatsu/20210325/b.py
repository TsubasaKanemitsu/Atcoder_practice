o = input()
e = input()

if len(o) - len(e) == 0:
    ans = ''
    for i in range(len(o)):
        ans += o[i] + e[i]
else:
    ans = ''
    for i in range(len(e)):
        ans += o[i] + e[i]
    ans += o[-1]

print(ans)