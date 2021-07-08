s = input()
t = input()

judge = [[0] * 26 for _ in range(26)]

for i in range(len(s)):
    ss = ord(s[i]) - ord('a') 
    tt = ord(t[i]) - ord('a')
    judge[ss][tt] = 1

for i in range(26):
    if sum(judge[i]) > 1:
        print("No")
        exit()

for i in range(26):
    cnt = 0
    for j in range(26):
        cnt += judge[j][i]
    if cnt > 1:
        print("No")
        exit()
print("Yes")