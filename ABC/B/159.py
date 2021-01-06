s = input()
n = len(s)
if s[0:int((n - 1) / 2 )] == s[int((n + 3) / 2) - 1:]:
    print("Yes")
else:
    print("No")