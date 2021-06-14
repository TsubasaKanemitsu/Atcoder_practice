s = list(input())

a = 0
z = len(s)

for i in range(len(s)):
    if s[i] == 'A':
        break
    else:
        a += 1

for i in range(len(s) - 1, -1, -1):
    if s[i] == 'Z':
        break
    else:
        z -= 1

print(z - a)