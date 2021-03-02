from collections import Counter
s = input()
t = input()

flag = True
atcoder = ['a', 't', 'c', 'o', 'd', 'e', 'r']
for i in range(len(s)):
    if s[i] == t[i] or (s[i] == '@' and t[i] in atcoder) or (t[i] == '@' and s[i] in atcoder):
        pass
    else:
        flag = False

if flag:
    print("You can win")
else:
    print("You will lose")
