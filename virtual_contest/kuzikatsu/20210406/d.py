s = int(input())

ss = s

cnt = 0
i = 1
while s // i >= 3:
    i += 1
    cnt += 1
# print(cnt)

ans = 0
for i in range(1, cnt + 1):
    ans += (s // i - 3) * i
print(ans)