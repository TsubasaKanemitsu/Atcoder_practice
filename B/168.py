k = int(input())
s = input()

if len(s) <= k:
    print(s)
else:
    s = s[0:k] + '...'
    print(s)
