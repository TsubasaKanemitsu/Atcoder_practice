s = input()
result = 'WA'
if s[0] == 'A' and s[2:-1].count('C') == 1:
    s = s.replace('A', '')
    s = s.replace('C', '')
    if s.islower():
        result = 'AC'
print(result)