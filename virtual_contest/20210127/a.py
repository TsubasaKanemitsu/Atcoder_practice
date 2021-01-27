s = list(input())
l = len(s)
num = s.count('o')

ans = 15 - l + num

if ans >= 8:
    print("YES")
else:
    print("NO")