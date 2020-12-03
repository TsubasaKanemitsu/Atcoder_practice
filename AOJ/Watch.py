S = int(input())

h = 0
m = 0
s = 0
for i in range(1, S + 1):
    s += 1
    if s >= 60:
        m += 1
        s = 0
        if m >= 60:
            h += 1
            m = 0

print(f'{h}:{m}:{s}')
