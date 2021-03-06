# 部分文字列のパターンマッチ
s = input()

t = "abcdefghijklmnopqrstuvwxyz."

def is_match(t, s):
    # 比較するときにSの終点より，Tの長さ分手前から比較する必要があるから
    for i in range(len(s) - len(t) + 1):
        flag = True
        for j in range(len(t)):
            if s[i + j] != t[j] and t[j] != '.':
                flag = False
        if flag:
            return True
    return False


# 1文字
ans = []
for tt in t:
    if is_match(tt, s):
        ans.append(tt)

for tt1 in t:
    for tt2 in t:
        if is_match(tt1 + tt2, s):
            ans.append(tt1 + tt2)

for tt1 in t:
    for tt2 in t:
        for tt3 in t:
            if is_match(tt1 + tt2 + tt3, s):
                ans.append(tt1 + tt2 + tt3)
print(len(ans))