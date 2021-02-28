n = int(input())
s = input()

black_cnt = 0
white_cnt = s.count('.')
ans = black_cnt + white_cnt
for i in range(n):
    if s[i] == '#':
        black_cnt += 1
    else:
        white_cnt -= 1
    ans = min(ans, black_cnt + white_cnt)
print(ans)