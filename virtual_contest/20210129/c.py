import re
s = input()
if re.fullmatch(r'A?KIHA?BA?RA?', s):
    print("YES")
else:
    print("NO")