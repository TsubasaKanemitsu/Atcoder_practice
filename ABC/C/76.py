s_dash = input()
t = input()

ans = []
for i in range(len(s_dash) - len(t) + 1):
    word = ''
    flag = True
    for j in range(len(t)):
        # 1度でも一致しない箇所があれば、条件を満たさない
        if s_dash[i + j] != '?' and s_dash[i + j] != t[j]:
            flag = False
    if flag:
        word = s_dash[0:i] + t + s_dash[i + j + 1:]
        ans.append(word.replace('?', 'a'))

ans.sort()

if len(ans) == 0:
    print("UNRESTORABLE")
else:
    print(ans[0])