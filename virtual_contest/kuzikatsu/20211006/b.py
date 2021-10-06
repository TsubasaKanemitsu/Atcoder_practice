h, w = list(map(int, input().split()))
S = [list(input()) for _ in range(h)]

ans = 0
for i in range(h):
    for j in range(w):
        if j < w - 1:
            if S[i][j] == '.' and S[i][j + 1] == '.':
                ans += 1
        if i < h - 1:
            if S[i][j] == '.' and S[i + 1][j] == '.':
                ans += 1
print(ans)