# 解説見てもわからん
# また今度見直し
# https://drken1215.hatenablog.com/entry/2020/11/11/203000
s = input()
k = int(input())

cnt = 0
a = 0
b = 0

for i in range(1, len(s)):
    if s[0] == s[i]:
        a += 1
    else:
        break
for i in range(len(s)):
    if s[len(s) - 1] == s[- i - 1]:
        b += 1
    else:
        break
if a == len(s):
    print(a * k // 2)
    exit()
    
tmp_cnt = 1
for i in range(len(s) - 1):   
    if s[i] == s[i + 1]:
        tmp_cnt += 1
    else:
        cnt += tmp_cnt // 2
        tmp_cnt = 1

if s[0] != s[-1]:
    print(cnt * k)
else:
    ans = cnt * k + (k - 1) * ((a + b) // 2) + (a // 2 + b // 2)
    print(ans)