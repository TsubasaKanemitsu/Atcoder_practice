# 全探索
s = list(input())

c = set()
q = set()
no = set()

for i in range(len(s)):
    if s[i] == 'o':
        c.add(str(i))
    elif s[i] == '?':
        q.add(str(i))
    else:
        no.add(str(i))

ans = 0
for i in range(10 ** 4):
    number = list(str(i).zfill(4))
    # 存在しない暗証番号が含まれているかを判定
    flag1 = False
    for n in number:
        if n in no:
            flag1 = True
            break
    if flag1:
        continue

    # 覚えている暗証番号が全て入っている
    flag2 = False
    if set(number) & c == c:
        flag2 = True

    if flag2:
        ans += 1

print(ans)
