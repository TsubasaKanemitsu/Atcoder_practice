# 2分半
s = input()

cnt = 0
for i in range(len(s)):
    temp_cnt = 0
    for i in range(i, len(s)):
        if s[i] in ['A', 'C', 'G', 'T']:
            temp_cnt += 1
        else:
            break
    cnt = max(cnt, temp_cnt)
print(cnt)