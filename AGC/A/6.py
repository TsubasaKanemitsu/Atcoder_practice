n = int(input())
s = input()
t = input()

if s == t:
    print(len(s))
    exit()

match_cnt = 0
cnt = 0
for i in range(len(s)):
    for j in range(len(s) - i):
        if s[i + j] != t[j]:
            cnt += 1
            match_cnt = 0
            break
        else:
            match_cnt += 1
    if match_cnt == len(s) - i:
        break
ans = cnt + match_cnt + len(t) - match_cnt

print(ans)

# 他の解答でわかりやすいもの
# N = int(input())
# s = input()
# t = input()
# if s == t:
#     print(N)
#     exit()
# c = 0
# for i in range(N):
#     if s[i:] == t[:-i]:
#         c = i
#         break
# if c:
#     print(c + (N - c) + c)
# else:
#     print(N + N)