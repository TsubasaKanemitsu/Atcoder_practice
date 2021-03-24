# 40分
N = int(input())
S = input()

west = []
east = []

if S[0] == 'W':
    west.append(1)
    east.append(0)
else:
    west.append(0)
    east.append(1)

for i in range(1, N):
    if S[i] == 'W':
        west.append(west[i - 1] + 1)
        east.append(east[i - 1])
    else:
        west.append(west[i - 1])
        east.append(east[i - 1] + 1)
ans = 10 ** 100
for i in range(N):
    if S[i] == 'W':
        person = (east[N - 1] - east[i]) + west[i] - 1
    else:
        person = (east[N - 1] - east[i]) + west[i]
    
    ans = min(ans, person)
print(ans)