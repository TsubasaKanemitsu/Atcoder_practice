n = int(input())
s = input()

slim = []

# 同じ文字列
if len(list(set(s))) == 1:
    print(1)

else:
    for i in range(n):
        if s[i] != s[i + 1]:
            slim.append(s[i])
    slim.append(s[n - 1])
    print(len(slim))