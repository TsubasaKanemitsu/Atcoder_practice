s = list(input())
t = list(input())

# print(s)
# print(t)
result = "No"
for i in range(len(s)):
    _s = s[i:] + s[0:i]
    for j in range(len(t)):
        _t = t[j:] + t[0:j]
        if ''.join(_s) < ''.join(_t):
            result = "Yes"
            break
print(result)