o = input()
e = input()

ans = ''
if len(o) - len(e) == 0:
    for i in range(len(o)):
        ans += o[i] + e[i]
    print(ans)
else:
    for i in range(len(o) - 1):
        ans += o[i] + e[i]
    ans += o[len(o) - 1]
    print(ans)