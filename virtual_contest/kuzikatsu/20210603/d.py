s = list(input())
ans = 0
for bit in range(1 << len(s)):
    st = 0
    temp_ans = 0
    num = '0'
    for i in range(len(s)):
        if bit & 1 << i:
            temp_ans += int(num)
            num = '0'
        else:
            num += str(s[i])
    temp_ans += int(num)
    ans += temp_ans
print(ans)