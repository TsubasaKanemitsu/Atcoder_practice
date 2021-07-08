# 5分
# 文字列の解を定義し、比較

s = input()


ans_s0 = ''
ans_s1 = ''
for i in range(len(s)):
    if i % 2 == 0:
        ans_s0 += '0'
        ans_s1 += '1'
    else:
        ans_s0 += '1'
        ans_s1 += '0'

ans0 = 0
ans1 = 0
for i in range(len(s)):
    if s[i] != ans_s0[i]:
        ans0 += 1
    if s[i] != ans_s1[i]:
        ans1 += 1
print(min(ans0, ans1))