S = [list(input()) for _ in range(2)]

ans = 0
for s in S:
    ans += s.count('#')

if ans >= 3:
    print("Yes")
    exit()

if(S[0][0] == '#' and S[1][1] == '#') or (S[0][1] == '#' and S[1][0] == '#'):
    print("No")
else:
    print("Yes")