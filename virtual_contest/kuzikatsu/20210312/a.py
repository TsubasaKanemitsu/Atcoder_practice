n = int(input())
s = input()

cnt = 0
for i in range(n):
    if s[i] == 'R':
        cnt += 1
    else:
        cnt -= 1

if cnt > 0:
    print("Yes")
else:
    print("No")