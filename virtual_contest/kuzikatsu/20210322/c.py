from collections import Counter
n, s = input().split()
n = int(n)

cnt = 0
# 同じ文字数が存在することを確認できればいい
for i in range(n):
    cnt1 = 0
    cnt2 = 0
    for j in range(i, n):
        if s[j] == 'A':
            cnt1 += 1
        elif s[j] == 'T':
            cnt1 -= 1
        elif s[j] == 'G':
            cnt2 += 1
        elif s[j] == 'C':
            cnt2 -= 1
        if cnt1 == 0 and cnt2 == 0:
            cnt += 1

print(cnt)