s = list(input())

if s[-1] == 's':
    s.append('es')
else:
    s.append('s')

print(''.join(s))