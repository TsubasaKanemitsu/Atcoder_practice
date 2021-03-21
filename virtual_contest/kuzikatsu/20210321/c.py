s = list(input())

ans = 0
black_cnt = 0
for i in range(len(s)):
    if s[i] == 'B':
        black_cnt += 1
    else:
        ans += black_cnt
print(ans)