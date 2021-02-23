n, k = list(map(int, input().split()))
r, s, p = list(map(int, input().split()))
t = input()

ans = 0
commands = [''] * n

for i, t in enumerate(t):
    if t == 'r':
        command = 'p'
        point = p
    elif t == 's':
        command = 'r'
        point = r
    else:
        command = 's'
        point = s
    
    if (i - k) >= 0 and (commands[i - k] == command):
        point = 0
        command = ''

    ans += point
    commands[i] = command
print(ans)
