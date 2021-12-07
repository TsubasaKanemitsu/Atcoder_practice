n = int(input())
S = [list(input()) for _ in range(n)]

# 各文字列のa ~ zの個数をカウントする
# 共通で有しているa ~ zとその文字列の最小数を求める
# [a ~ z] * nの配列に個数を与える

cnt = [[0] * n for _ in range(26)]
alphabet = [chr(i) for i in range(97, 97+26)]
for i in range(n):
    ss = S[i]
    for s in ss:
        for j in range(26):
            if s == alphabet[j]:
                cnt[j][i] += 1
            
ans = ''

for i in range(97, 97 + 26):
    ans += chr(i) * min(cnt[i - 97])

print(ans)
