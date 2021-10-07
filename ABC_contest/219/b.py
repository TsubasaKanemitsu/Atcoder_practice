S = [input() for _ in range(3)]
T = input()

ans = ''
for t in T:
    tt = int(t) - 1
    ans += S[tt]
print(ans)